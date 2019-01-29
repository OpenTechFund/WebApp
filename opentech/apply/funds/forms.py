from django import forms

from opentech.apply.users.models import User

from .models import ApplicationSubmission
from .utils import can_alter_reviewers, set_reviewers_fields
from .widgets import Select2MultiCheckboxesWidget


class ProgressSubmissionForm(forms.ModelForm):
    action = forms.ChoiceField(label='Take action')

    class Meta:
        model = ApplicationSubmission
        fields: list = []

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        choices = list(self.instance.get_actions_for_user(self.user))
        action_field = self.fields['action']
        action_field.choices = choices
        self.should_show = bool(choices)


class ScreeningSubmissionForm(forms.ModelForm):

    class Meta:
        model = ApplicationSubmission
        fields = ('screening_status',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.should_show = False
        if (self.instance.active and self.user.is_apply_staff) or self.user.is_superuser:
            self.should_show = True


class UpdateSubmissionLeadForm(forms.ModelForm):
    class Meta:
        model = ApplicationSubmission
        fields = ('lead',)

    def __init__(self, *args, **kwargs):
        kwargs.pop('user')
        super().__init__(*args, **kwargs)
        lead_field = self.fields['lead']
        lead_field.label = f'Update lead from { self.instance.lead } to'
        lead_field.queryset = lead_field.queryset.exclude(id=self.instance.lead.id)


class UpdateReviewersForm(forms.ModelForm):
    staff_reviewers = forms.ModelMultipleChoiceField(
        queryset=User.objects.staff(),
        widget=Select2MultiCheckboxesWidget(attrs={'data-placeholder': 'Staff'}),
        required=False,
    )
    reviewer_reviewers = forms.ModelMultipleChoiceField(
        queryset=User.objects.reviewers().exclude(id__in=User.objects.staff()),
        widget=Select2MultiCheckboxesWidget(attrs={'data-placeholder': 'Reviewers'}),
        label='Reviewers',
        required=False,
    )

    class Meta:
        model = ApplicationSubmission
        fields: list = []

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        submitted_reviewers, fields = set_reviewers_fields(self.instance, self.user, self.fields)
        self.submitted_reviewers = submitted_reviewers
        self.fields = fields

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        if can_alter_reviewers(self.instance, self.user):
            reviewers = self.cleaned_data.get('reviewer_reviewers')
        else:
            reviewers = instance.reviewers_not_reviewed

        instance.reviewers.set(
            self.cleaned_data['staff_reviewers'] |
            reviewers |
            self.submitted_reviewers
        )
        return instance


class BatchUpdateReviewersForm(forms.Form):
    name = 'batch_reviewer_form'

    staff_reviewers = forms.ModelMultipleChoiceField(
        queryset=User.objects.staff(),
        widget=Select2MultiCheckboxesWidget(attrs={'data-placeholder': 'Staff'}),
        required=False,
    )
    submission_ids = forms.CharField(widget=forms.HiddenInput())

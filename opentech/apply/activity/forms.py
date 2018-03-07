from django import forms

from .models import Activity


class CommentForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('message', 'visibility')
        labels = {
            'visibility': '',
        }
        widgets = {
            'visibility': forms.RadioSelect(),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.visibility_choices = self._meta.model.visibility_choices_for(user)
        if len(self.visibility_choices) > 1:
            self.fields['visibility'].choices = self.visibility_choices
        else:
            self.fields['visibility'].widget = forms.HiddenInput()

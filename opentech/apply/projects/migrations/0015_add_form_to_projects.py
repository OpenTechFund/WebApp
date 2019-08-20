# Generated by Django 2.0.13 on 2019-08-12 00:55

import django.contrib.postgres.fields.jsonb
from django.db import migrations
import opentech.apply.stream_forms.blocks
import opentech.apply.stream_forms.files
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('application_projects', '0014_projectapprovalform'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='form_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, encoder=opentech.apply.stream_forms.files.StreamFieldDataEncoder),
        ),
        migrations.AddField(
            model_name='project',
            name='form_fields',
            field=wagtail.core.fields.StreamField([('text_markup', wagtail.core.blocks.RichTextBlock(group='Custom', label='Section text/header')), ('char', wagtail.core.blocks.StructBlock([('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('format', wagtail.core.blocks.ChoiceBlock(choices=[('email', 'Email'), ('url', 'URL')], label='Format', required=False)), ('default_value', wagtail.core.blocks.CharBlock(label='Default value', required=False))], group='Fields')), ('text', wagtail.core.blocks.StructBlock([('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.TextBlock(label='Default value', required=False))], group='Fields')), ('number', wagtail.core.blocks.StructBlock([('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.CharBlock(label='Default value', required=False))], group='Fields')), ('checkbox', wagtail.core.blocks.StructBlock([('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.BooleanBlock(required=False))], group='Fields')), ('radios', wagtail.core.blocks.StructBlock([('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('choices', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Choice')))], group='Fields')), ('dropdown', wagtail.core.blocks.StructBlock([('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('choices', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Choice')))], group='Fields')), ('checkboxes', wagtail.core.blocks.StructBlock([('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('checkboxes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Checkbox')))], group='Fields')), ('date', wagtail.core.blocks.StructBlock([('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.DateBlock(required=False))], group='Fields')), ('time', wagtail.core.blocks.StructBlock([('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.TimeBlock(required=False))], group='Fields')), ('datetime', wagtail.core.blocks.StructBlock([('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.core.blocks.DateTimeBlock(required=False))], group='Fields')), ('image', wagtail.core.blocks.StructBlock([('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False))], group='Fields')), ('file', wagtail.core.blocks.StructBlock([('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False))], group='Fields')), ('multi_file', wagtail.core.blocks.StructBlock([('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(label='Required', required=False))], group='Fields')), ('group_toggle', wagtail.core.blocks.StructBlock([('field_label', wagtail.core.blocks.CharBlock(label='Label')), ('help_text', wagtail.core.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.core.blocks.BooleanBlock(default=True, label='Required')), ('choices', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label='Choice'), help_text='Please create only two choices for toggle. First choice will revel the group and the second hide it. Additional choices will be ignored.'))], group='Custom')), ('group_toggle_end', opentech.apply.stream_forms.blocks.GroupToggleEndBlock(group='Custom'))], null=True),
        ),
    ]

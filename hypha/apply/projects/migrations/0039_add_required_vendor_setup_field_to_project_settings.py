# Generated by Django 2.2.24 on 2021-06-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_projects', '0038_rename_verbose_name_of_vendor_form_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsettings',
            name='vendor_setup_required',
            field=models.BooleanField(default=True),
        ),
    ]
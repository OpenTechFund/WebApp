# Generated by Django 2.0.13 on 2019-09-06 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_projects', '0019_add_paid_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsettings',
            name='finance_email',
            field=models.TextField(default='', verbose_name='Finance Email'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.24 on 2021-07-08 08:24

from decimal import Decimal
from django.conf import settings
import django.core.files.storage
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import hypha.apply.projects.models.payment


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application_projects', '0041_add_user_has_updated_details_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('paid_value', models.DecimalField(decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('document', models.FileField(storage=django.core.files.storage.FileSystemStorage(), upload_to=hypha.apply.projects.models.payment.invoice_path)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('message_for_pm', models.TextField(blank=True)),
                ('comment', models.TextField(blank=True)),
                ('status', models.TextField(choices=[('submitted', 'Submitted'), ('changes_requested', 'Changes Requested'), ('under_review', 'Under Review'), ('paid', 'Paid'), ('declined', 'Declined')], default='submitted')),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='application_projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='SupportingDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(storage=django.core.files.storage.FileSystemStorage(), upload_to='supporting_documents')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supporting_documents', to='application_projects.Invoice')),
            ],
        ),
    ]

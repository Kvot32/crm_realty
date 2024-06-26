# Generated by Django 5.0.6 on 2024-05-24 05:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_feedback_client_alter_feedback_application'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='deals', to='client.client'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deal',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals', to='client.application'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='responsible_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals', to='employee.employee'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-22 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

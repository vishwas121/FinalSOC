# Generated by Django 2.2.3 on 2019-07-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_circulation_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circulation',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

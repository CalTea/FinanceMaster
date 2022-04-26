# Generated by Django 4.0.3 on 2022-04-24 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinanceMasterApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=30),
        ),
        migrations.AlterField(
            model_name='asset',
            name='qty',
            field=models.DecimalField(decimal_places=1, max_digits=999),
        ),
    ]

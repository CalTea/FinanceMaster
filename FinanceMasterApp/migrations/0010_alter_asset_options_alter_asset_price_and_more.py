# Generated by Django 4.0.3 on 2022-04-25 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinanceMasterApp', '0009_remove_asset_total'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={'ordering': ['-price']},
        ),
        migrations.AlterField(
            model_name='asset',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=30),
        ),
        migrations.AlterField(
            model_name='asset',
            name='qty',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-13 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_alter_product_formule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='uom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='records.uom', verbose_name='Unité'),
        ),
    ]

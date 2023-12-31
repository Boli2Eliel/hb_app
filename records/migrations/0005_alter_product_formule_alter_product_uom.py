# Generated by Django 4.2.4 on 2023-09-13 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_alter_product_uom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='formule',
            field=models.ForeignKey(default='None', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='products', to='records.formule', verbose_name='Formule'),
        ),
        migrations.AlterField(
            model_name='product',
            name='uom',
            field=models.ForeignKey(default='None', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='products', to='records.uom', verbose_name='Unité'),
        ),
    ]

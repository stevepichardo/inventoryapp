# Generated by Django 3.1.4 on 2021-01-04 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemForm', '0002_item_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='purchase_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='sold_date',
            field=models.DateField(blank=True),
        ),
    ]

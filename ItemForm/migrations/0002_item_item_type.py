# Generated by Django 3.1.4 on 2021-01-04 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemForm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('expense_type', 'expense'), ('income_type', 'income')], default='expense', max_length=15),
        ),
    ]

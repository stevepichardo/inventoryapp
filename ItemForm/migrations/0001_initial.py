# Generated by Django 3.1.4 on 2021-01-02 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('purchase_date', models.DateField()),
                ('profit', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sold_date', models.DateField()),
            ],
        ),
    ]

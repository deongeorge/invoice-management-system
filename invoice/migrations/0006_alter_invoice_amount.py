# Generated by Django 3.2.5 on 2021-07-04 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_delete_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='Amount',
            field=models.IntegerField(blank=True, choices=[('40000', '40000'), ('60000', '60000'), ('80000', '80000'), ('100000', '100000'), ('125000', '125000'), ('150000', '150000')], null=True),
        ),
    ]

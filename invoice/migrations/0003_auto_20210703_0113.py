# Generated by Django 3.2.5 on 2021-07-02 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20210702_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='Payment_Link',
        ),
        migrations.AddField(
            model_name='invoice',
            name='Payment_link',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='Client_email',
            field=models.EmailField(default='', max_length=50, unique=True),
        ),
    ]

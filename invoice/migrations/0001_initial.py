# Generated by Django 3.2.5 on 2021-07-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Invoice_number', models.IntegerField(blank=True, null=True)),
                ('Client_name', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('Client_email', models.EmailField(blank=True, default='', max_length=254, null=True)),
                ('Project_name', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('Amount', models.IntegerField(blank=True, null=True)),
                ('line_one', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Line 1')),
                ('line_one_quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity')),
                ('line_one_unit_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (D)')),
                ('line_one_total_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)')),
                ('line_two', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Line 1')),
                ('line_two_quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity')),
                ('line_two_unit_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (D)')),
                ('line_two_total_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)')),
                ('line_three', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Line 1')),
                ('line_three_quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity')),
                ('line_three_unit_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (D)')),
                ('line_three_total_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)')),
                ('line_four', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Line 1')),
                ('line_four_quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity')),
                ('line_four_unit_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (D)')),
                ('line_four_total_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)')),
                ('line_five', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Line 1')),
                ('line_five_quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity')),
                ('line_five_unit_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Unit Price (D)')),
                ('line_five_total_price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)')),
                ('phone_number', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Line 1')),
                ('total', models.IntegerField(blank=True, default=0, null=True)),
                ('balance', models.IntegerField(blank=True, default=0, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('invoice_type', models.CharField(blank=True, choices=[('Receipt', 'Receipt'), ('Proforma Invoice', 'Proforma Invoice'), ('Invoice', 'Invoice')], default='', max_length=50, null=True)),
            ],
        ),
    ]

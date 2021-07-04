from django.db import models


class Invoice(models.Model):
    Invoice_number = models.IntegerField(blank=True, null=True)
    Client_name = models.CharField(max_length=30, default='', blank=True, null=True)
    Client_email = models.EmailField(max_length=50, unique=True ,default='')
    Project_name = models.CharField(max_length=300, default='', blank=True, null=True)
    Amount_choice = (
        ('40000','40000'),
        ('60000','60000'),
        ('80000','80000'),
        ('100000','100000'),
        ('125000','125000'),
        ('150000','150000'),
    )
    Amount = models.CharField(max_length=30, blank=True, null=True ,choices=Amount_choice)
    Payment_link =models.CharField(max_length=100, default='', blank=True, null=True)


    def __str__(self):
        return self.Client_name + '-' +str(self.Invoice_number)

    def __unicode__(self):
        return self.Invoice_number



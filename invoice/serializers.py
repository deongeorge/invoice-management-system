from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('Invoice_number','Client_name','Client_email',
                  'Project_name', 'Amount')
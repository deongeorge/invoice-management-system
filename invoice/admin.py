from django.contrib import admin
from .models import Invoice
from .forms import InvoiceForm



class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['Invoice_number','Client_name', 'Project_name','Amount']
    form = InvoiceForm
    list_filter = ['Project_name','Client_name']
    search_fields = ['Client_name','Invoice_number','Project_name']


admin.site.register(Invoice, InvoiceAdmin)





from django import forms

from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['Invoice_number','Client_name','Client_email',
                  'Project_name', 'Amount','Payment_link']

    def clean_Invoice_number(self):
        Invoice_number = self.cleaned_data.get('Invoice_number')
        if not Invoice_number:
            raise forms.ValidationError('This field is required')
        return Invoice_number

    def clean_Client_name(self):
        Client_name = self.cleaned_data.get('Client_name')
        if not Client_name:
            raise forms.ValidationError("This field is required")
        return Client_name

    def clean_Project_name(self):
        Project_name = self.cleaned_data.get('Project_name')
        if not Project_name:
            raise forms.ValidationError("This field is required")
        return Project_name

    def clean_Amount(self):
        Amount = self.cleaned_data.get('Amount')

        return Amount

    def clean_Payment_link(self):
        Payment_link = self.cleaned_data.get('Amount')
        if not Payment_link:
            raise forms.ValidationError("This field is required")
        return Payment_link



class InvoiceSearchForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['Invoice_number', 'Client_name']


class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['Invoice_number','Client_name','Client_email',
                  'Project_name', 'Amount','Payment_link']
    def clean_Invoice_number(self):
        Invoice_number = self.cleaned_data.get('Invoice_number')
        if not Invoice_number:
            raise forms.ValidationError('This field is required')
        return Invoice_number

    def clean_Client_name(self):
        Client_name = self.cleaned_data.get('Client_name')
        if not Client_name:
            raise forms.ValidationError("This field is required")
        return Client_name

    def clean_Project_name(self):
        Project_name = self.cleaned_data.get('Project_name')
        if not Project_name:
            raise forms.ValidationError("This field is required")
        return Project_name

    def clean_Amount(self):
        Amount = self.cleaned_data.get('Amount')
        if not Amount:
            raise forms.ValidationError("This field is required")
        return Amount

    def clean_Payment_link(self):
        Payment_link = self.cleaned_data.get('Amount')
        if not Payment_link:
            raise forms.ValidationError("This field is required")
        return Payment_link
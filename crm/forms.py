# crm/forms.py
from django import forms
from .models import Customer, Deal

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'company']

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['customer', 'title', 'amount', 'stage']

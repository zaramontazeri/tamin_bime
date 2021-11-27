from django import forms
from .models import Wallets, Transactions, Invoice


class WalletsForm(forms.ModelForm):
    class Meta:
        model = Wallets
        fields = ['value', 'user']


class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = '__all__'


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'



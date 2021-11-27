from django.contrib import admin
from django import forms
from .models import Wallets, Transaction, Invoice

class WalletsAdminForm(forms.ModelForm):

    class Meta:
        model = Wallets
        fields = '__all__'


class WalletsAdmin(admin.ModelAdmin):
    form = WalletsAdminForm
    list_display = ['created', 'last_updated', 'value']
    readonly_fields = ['created', 'last_updated']

admin.site.register(Wallets, WalletsAdmin)


class TransactionsAdminForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionsAdmin(admin.ModelAdmin):
    form = TransactionsAdminForm
    list_display = ['created', 'last_updated']
    readonly_fields = ['created', 'last_updated']

admin.site.register(Transaction, TransactionsAdmin)


class InvoiceAdminForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceAdmin(admin.ModelAdmin):
    form = InvoiceAdminForm
    list_display = ['created', 'last_updated']
    readonly_fields = ['created', 'last_updated']

admin.site.register(Invoice, InvoiceAdmin)



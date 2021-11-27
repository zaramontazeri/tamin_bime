import unittest
from django.urls import reverse
from django.test import Client
from .models import Wallets, Transactions, Invoice
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_wallets(**kwargs):
    defaults = {}
    defaults["value"] = "value"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return Wallets.objects.create(**defaults)


def create_transactions(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return Transactions.objects.create(**defaults)


def create_invoice(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return Invoice.objects.create(**defaults)


class WalletsViewTest(unittest.TestCase):
    '''
    Tests for Wallets
    '''
    def setUp(self):
        self.client = Client()

    def test_list_wallets(self):
        url = reverse('user_info_wallets_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_wallets(self):
        url = reverse('user_info_wallets_create')
        data = {
            "value": "value",
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_wallets(self):
        wallets = create_wallets()
        url = reverse('user_info_wallets_detail', args=[wallets.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_wallets(self):
        wallets = create_wallets()
        data = {
            "value": "value",
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('user_info_wallets_update', args=[wallets.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TransactionsViewTest(unittest.TestCase):
    '''
    Tests for Transactions
    '''
    def setUp(self):
        self.client = Client()

    def test_list_transactions(self):
        url = reverse('user_info_transactions_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_transactions(self):
        url = reverse('user_info_transactions_create')
        data = {
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_transactions(self):
        transactions = create_transactions()
        url = reverse('user_info_transactions_detail', args=[transactions.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_transactions(self):
        transactions = create_transactions()
        data = {
        }
        url = reverse('user_info_transactions_update', args=[transactions.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class InvoiceViewTest(unittest.TestCase):
    '''
    Tests for Invoice
    '''
    def setUp(self):
        self.client = Client()

    def test_list_invoice(self):
        url = reverse('user_info_invoice_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_invoice(self):
        url = reverse('user_info_invoice_create')
        data = {
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_invoice(self):
        invoice = create_invoice()
        url = reverse('user_info_invoice_detail', args=[invoice.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_invoice(self):
        invoice = create_invoice()
        data = {
        }
        url = reverse('user_info_invoice_update', args=[invoice.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)



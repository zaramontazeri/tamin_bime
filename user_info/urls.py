from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'wallets', api.WalletsViewSet)
router.register(r'transactions', api.TransactionViewSet)
router.register(r'invoice', api.InvoiceViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)

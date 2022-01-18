from django.urls import path, include
from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register(r'companyreport', api.CompanyReportViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)
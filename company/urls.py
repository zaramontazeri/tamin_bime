from django.urls import path, include
from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register(r'company', api.CompanyViewSet)
router.register(r'file', api.File_CompanyViewSet)
router.register(r'insurance', api.InsuranceFormViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
    path("statistic/",api.RegistrationStatisticalApiView.as_view())
)
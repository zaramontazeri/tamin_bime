from django.urls import path, include
from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register(r'company', api.CompanyViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
    path("statistic/",api.RegistrationStatisticalApiView.as_view())
)
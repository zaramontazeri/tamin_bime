from django.urls import path, include
from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register(r'company', api.CompanyViewSet)
router.register(r'file', api.File_CompanyViewSet)
router.register(r'insurance', api.InsuranceFormViewSet)
router.register(r'insuranceformupload', api.InsuranceFormUploadViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path("statistic/",api.RegistrationStatisticalApiView.as_view()),
    path("user_company/",api.UserCompanyAPIView.as_view()),
    path('', include(router.urls)),

)
from django.urls import path, include
from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register(r'person', api.PersonViewSet)
router.register(r'file', api.File_PersonViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('registration/',api.RegistrationApiView.as_view()),
    path('', include(router.urls)),
    
)
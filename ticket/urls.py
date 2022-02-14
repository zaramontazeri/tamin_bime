from django.urls import path, include
from rest_framework import routers
from . import api

router= routers.DefaultRouter()
router.register(r'thread', api.ThreadViewSet)
router.register(r'message', api.MessageViewSet)

urlpatterns=(
    path('',include(router.urls)),
)
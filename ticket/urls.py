from django.urls import path, include
from rest_framework import routers
from . import api

router= routers.DefaultRouter()
router.register(r'thread', api.ThreadViewSet)
router.register(r'message', api.MessageViewSet)

urlpatterns=(
    path('',include(router.urls)),
    path("users_list/",api.UsersListApiView.as_view()),
    # path("messages_list_thread/",api.MessageListThreadApiView.as_view()),
    # path("messages_list_user_id/",api.MessageListUserIdApiView.as_view()),
)
from xml.dom import ValidationErr
from django import views

from django.http import QueryDict
from . import models
from . import serializers
from rest_framework import viewsets, permissions, response, status , exceptions, views
from auth_rest_phone import models as amodels
from auth_rest_phone import serializers as aserializers
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from role_manager.permissions import HasGroupRolePermission

class ThreadViewSet(viewsets.ModelViewSet):
    queryset=models.Thread.objects.all()
    serializer_class=serializers.ThreadSerializer
    permission_classes=[permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data=dict(request.data)
        
        if request.user.is_superuser :
            data["user2"]=request.user.id
            data["user1"]=data.get('user1')
        else:
            data['user1']=request.user.id
            superusers=amodels.UserProfile.objects.filter(is_superuser=True)
            user = [{"id":i.id } for i in superusers][0]
            data['user2']=user['id']
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class MessageViewSet(viewsets.ModelViewSet):
    queryset=models.Message.objects.all()
    serializer_class=serializers.MessageSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes=[permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user=request.user
        thread_id=request.data.get('thread',None)
        thread = 0
        data = request.data
        if(thread_id==None):
            assert exceptions.ValidationError(detail="please enter thread id  ", code="thread_id_missed")
        try :
            thread=models.Thread.objects.get(id=thread_id)
        except  models.Thread.DoesNotExist:
            assert exceptions.NotFound(
                detail="thread not found", code="thread_not_found"
            )
        #add this becuase of front dont send direction and its get error
        data._mutable = True
        
        user1 = thread.user1
        user2=thread.user2
        if user == user1:
            data["direction"] = 'u1tou2'
        elif user==user2 :
            data["direction"] = 'u2tou1'
        request.data._mutable = False

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UsersListApiView(views.APIView):
    """APIView for the List Users -> post user_id"""
    permission_classes=[permissions.IsAuthenticated,HasGroupRolePermission]
    def post(self, request):
        user_id = request.query_params.get("user_id", 0)
        
        if user_id!=0:
            user=amodels.UserProfile.objects.filter(id=user_id)
            user_ser=aserializers.UserSerializer(user,many=True)
            return response.Response(user_ser.data)
        else:
            user=amodels.UserProfile.objects.all()
            user_ser=aserializers.UserSerializer(user,many=True)
            return response.Response(user_ser.data)
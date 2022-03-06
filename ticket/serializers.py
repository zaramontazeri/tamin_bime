from . import models
from rest_framework import serializers
from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from django.contrib.auth import  get_user_model
from auth_rest_phone.conf import settings
from drf_extra_fields.fields import Base64ImageField

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField(required=False)
    company_names = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD, "email", "first_name", "last_name", "avatar","id",'company_names'
        )
        read_only_fields = (settings.LOGIN_FIELD,)
    def get_company_names(self,obj):
        companies = obj.companies.all() 
        company_names = [ i.name for i in companies]
        return company_names



class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Message
        fields=(
            'pk',
            'created',
            'last_updated',
            'message',
            'file',
            'status',
            'direction',
            'thread'
        )


class ThreadSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)
    user1= PresentablePrimaryKeyRelatedField(
        queryset=User.objects.all(),
        presentation_serializer=UserSerializer,
        
        read_source=None
    )
    user2= PresentablePrimaryKeyRelatedField(
        queryset=User.objects.all(),
        presentation_serializer=UserSerializer,
        read_source=None
    )
    class Meta:
        model=models.Thread
        fields=(
            'pk',
            'created',
            'category',
            'user1',
            'user2',
            'ticket_id',
            'messages'
        )
        read_only_fields = ('ticket_id',)


from django.contrib import admin
from . import models
from django import forms

class ThreadAdminForm(forms.ModelForm):
    model=models.Thread
    fields='__all__'

class ThreadAdmin(admin.ModelAdmin):
    class Meta:
        form=ThreadAdminForm
        list_display=['created','category','ticket_id','user1','user2'] 
        readonly_fields=['created',]

admin.site.register(models.Thread,ThreadAdmin)

class MessageAdminForm(forms.ModelForm):
    model=models.Message
    fields='__all__'

class MessageAdmin(admin.ModelAdmin):
    class Meta:
        form=MessageAdminForm
        list_display=['created','last_updated','message','file','status','direction','thread']
        readonly_fields=['created','last_updated']

admin.site.register(models.Message,MessageAdmin)

from http.client import ResponseNotReady
from django import views
from . import models
from . import serializers
from rest_framework import viewsets, permissions, views, response
from datetime import datetime, time , timedelta 
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from role_manager.permissions import HasGroupRolePermission
from django.contrib.gis.db import models as gmodels

class PersonViewSet(viewsets.ModelViewSet):
    """ViewSet for the Person class"""
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    permission_classes = [permissions.IsAuthenticated,HasGroupRolePermission]

    def get_queryset(self):
        groups = self.request.user.groups.all()
        user = self.request.user
        if user.is_superuser :
            queryset = models.Person.objects.all()
        elif "marketer" in groups:
            queryset = models.Person.objects.filter(company__user = user)
        else :
            queryset = []
        # if isinstance(queryset, QuerySet):
        #     # Ensure queryset is re-evaluated on each request.
        #     queryset = queryset.all()
        return queryset

class File_PersonViewSet(viewsets.ModelViewSet):
    """ViewSet for the File class"""

    queryset = models.File_Person.objects.all()
    serializer_class = serializers.File_PersonSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = [permissions.IsAuthenticated,HasGroupRolePermission]

class RegistrationApiView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    # serializer_class = serializers.PersonSerializer
    def post(self,request):
        company_id = request.query_params.get("company_id", 0)
        try:
            from_date=datetime.strptime(self.request.data["from_date"],'%Y-%m-%d')
        except KeyError:
            raise ValidationError(code="from_date_required",detail=("please enter from date"))
        try :
            to_date=datetime.strptime(self.request.data["to_date"],'%Y-%m-%d')
        except KeyError:
            to_date =datetime.strptime( self.request.data.get("to_date",datetime.now().strftime("%Y-%m-%d")),'%Y-%m-%d')
        from_date = from_date.replace(hour=0, minute=0, second=0, microsecond=0)
        to_date = to_date.replace(hour=23,minute=59,second=59,microsecond=0)
        fromDate=from_date
        toDate=to_date
        date_list=[]
        while fromDate<=toDate:
            _from_date = fromDate.replace(hour=0, minute=0, second=0, microsecond=0)
            _to_date = fromDate.replace(hour=23, minute=59, second=59, microsecond=0)

            date_list.append((_from_date,_to_date))
            fromDate += timedelta(days=1)
        print(date_list)
        date_countPerson=[]
        if company_id!=0:
            for date in date_list:
                persons_count = models.Person.objects.filter(created__gte=date[0], created__lte=date[1], company=company_id).count()
                date_countPerson.append ({"date":date,"count person":persons_count})
            return response.Response(date_countPerson)
        else:
            for date in date_list:
                persons_count = models.Person.objects.filter(created__gte=date[0], created__lte=date[1],).count()
                date_countPerson.append ({"date":date,"count person":persons_count})
            return response.Response(date_countPerson)
        # if company_id!=0:
        #     persons_count = models.Person.objects.filter(created__gte = from_date , created__lte = to_date, company=company_id).count()
            
        # else:
        #     persons_count = models.Person.objects.filter(created__gte = from_date , created__lte = to_date).count()
        # return response.Response({"count":persons_count})
# def get_queryset(from_date,to_date):
#         from_date=datetime.strptime(from_date,'%Y-%m-%d')
        
#         to_date =datetime.strptime( to_date,'%Y-%m-%d')

#         from_date = from_date.replace(hour=0, minute=0, second=0, microsecond=0)
#         to_date = to_date.replace(hour=23,minute=59,second=59,microsecond=0)
#         return models.Person.objects.filter(created__gte = from_date , created__lte = to_date).count()


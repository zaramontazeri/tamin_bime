from datetime import date, datetime,timedelta
from . import models
from . import serializers
from rest_framework import viewsets, permissions,views,response
from django.db import models as dj_models
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from person import models as pmodels

def get_week():
    today=date.today()
    week_label ={7:"shanbe",1:"yekshanbe",2:"doshanbe",3:"seshanbe",4:"chaharshanbe",5:"panjshanbe",6:"jomee"}
    days = []
    for day in range(7):
        today-=timedelta(days=1)
        weekday=(today.isoweekday() % 7) + 1
        print(week_label[weekday],today)
        days.append ({"day":week_label[weekday],"date":today})
        # print(week_label[day] ,getDate(day))
    return days


class CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for the Company class"""

    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

class File_CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for the File class"""

    queryset = models.File_Company.objects.all()
    serializer_class = serializers.File_CompanySerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = [permissions.IsAuthenticated]

class RegistrationStatisticalApiView(views.APIView):
    
    def get (self, request):
        companies = models.Company.objects.annotate(num_register=dj_models.Count('persons')).order_by('-num_register')[:5]
        result = {}
        
        result["best_companies"] = [{"name":i.name , "num_register":i.num_register} for i in companies]
        days = get_week()
        week_statistics = []
        for day in days :
            from_date=str(day["date"])
            from_date=datetime.strptime(from_date,'%Y-%m-%d')
            from_date = from_date.replace(hour=0, minute=0, second=0, microsecond=0)
            to_date=str(day["date"])
            to_date=datetime.strptime(to_date,'%Y-%m-%d')
            to_date = to_date.replace(hour=23,minute=59,second=59,microsecond=0)
            week_statistics.append({"week_day":day["day"],"count":pmodels.Person.objects.filter(created__gte = from_date , created__lte = to_date).count()})
        result["week_statistics"] = week_statistics
        return response.Response(result)
        
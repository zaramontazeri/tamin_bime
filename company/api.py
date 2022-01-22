from datetime import date, datetime
from . import models
from . import serializers
from rest_framework import viewsets, permissions,views,response
from django.db import models as dj_models
from person import models as per_models
class CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for the Company class"""

    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

class File_CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for the File class"""

    queryset = models.File_Company.objects.all()
    serializer_class = serializers.File_CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

class RegistrationStatisticalApiView(views.APIView):
    
    def get (self, request):
        companies = models.Company.objects.annotate(num_register=dj_models.Count('persons')).order_by('-num_register')[:5]
        result = {}
        # persons=per_models.Person.objects.annotate(num_register=dj_models.Count())
        # today=date.today()
        # weekday=(today.isoweekday() % 7) + 1
        # week_label ={7:"shanbe",1:"yekshanbe",2:"doshanbe",3:"seshanbe",4:"chaharshanbe",5:"panjshanbe",6:"jomee"}
        # for day in week_label:
        #     if day==weekday:
        #         return week_label[day]

        # def getDate(date):
        #     if date==7:
        #         firstDate=today
        #     else:
        #         firstDate=today-datetime.timedelta(days=date)
        #     for day in week_label:
        #         rooz= f"day : {week_label[day]} , date : {firstDate}"
        #         firstDate+=datetime.timedelta(days=1)
        #         print(rooz)

        # for day in week_label:
        #     if day==weekday:
        #         getDate(day)

        # ["شنبه","یکشنبه","دوشنبه","سه شنبه","چهارشنبه","پنجشنبه","جمعه"]
        result["best_companies"] = [{"name":i.name , "num_register":i.num_register} for i in companies]
        # result["week_statistics"] = []
        return response.Response(result)
        
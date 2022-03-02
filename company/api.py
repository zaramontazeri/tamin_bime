from datetime import date, datetime, timedelta

from role_manager.permissions import HasGroupRolePermission
from . import models
from . import serializers
from rest_framework import viewsets, permissions, views, response, status,exceptions
from django.db import models as dj_models
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser
from person import models as pmodels
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


def get_week():
    today = date.today()
    week_label = {7: "shanbe", 1: "yekshanbe", 2: "doshanbe",
                  3: "seshanbe", 4: "chaharshanbe", 5: "panjshanbe", 6: "jomee"}
    days = []
    for day in range(7):
        today -= timedelta(days=1)
        weekday = (today.isoweekday() % 7) + 1
        # print(week_label[weekday], today)
        days.append({"day": week_label[weekday], "date": today})
        # print(week_label[day] ,getDate(day))
    return days

class UserCompanyAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self, request):
        user=request.user
        try :
            company=models.Company.objects.filter(user=user)
            company_ser=serializers.CompanySerializer(company,many=True)
            return response.Response(company_ser.data)
        except models.Company.DoesNotExist:
            assert exceptions.NotFound(detail = "company does not found" , code="company_does_not_found")
            
class CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for the Company class
    dont get user, instead of that get password and re_password
    and username is readonly
    """

    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAuthenticated, HasGroupRolePermission]

    def create(self, request, *args, **kwargs):
        data = request.data
        user = {}
        user['first_name'] = data.get('manager_first_name')
        user['last_name'] = data.get('manager_last_name')
        user['phone'] = data.get('mobile_numbers')[0]
        user['email'] = data.get('email')
        user['password'] = data.pop('password')
        user['re_password'] = data.pop('re_password')
        user['username'] = data.get('manager_national_code')
        data['username'] = data.get('manager_national_code')
        data['user'] = user
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # new_user_id = serializer.data.user.id
        # new_user = User.objects.get(id=new_user_id)
        # try:
        #     gr, cr = Group.objects.get_or_create(name="marketer")
        #     gr.user_set.add(user)
        # except Exception as e:
        #     pass #group does not exist in context
        # user.is_active = True
        # user.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self,
            'groups': "marketer"
        }


class File_CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for the File class"""

    queryset = models.File_Company.objects.all()
    serializer_class = serializers.File_CompanySerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = [permissions.IsAuthenticated, HasGroupRolePermission]


class RegistrationStatisticalApiView(views.APIView):

    def get(self, request):
        companies = models.Company.objects.annotate(
            num_register=dj_models.Count('persons')).order_by('-num_register')[:5]
        result = {}

        result["best_companies"] = [
            {"company_id":i.id,"name": i.name, "num_register": i.num_register} for i in companies]
        days = get_week()
        week_statistics = []
        for day in days:
            from_date = str(day["date"])
            from_date = datetime.strptime(from_date, '%Y-%m-%d')
            from_date = from_date.replace(
                hour=0, minute=0, second=0, microsecond=0)
            to_date = str(day["date"])
            to_date = datetime.strptime(to_date, '%Y-%m-%d')
            to_date = to_date.replace(
                hour=23, minute=59, second=59, microsecond=0)
            week_statistics.append({"week_day": day["day"], "count": pmodels.Person.objects.filter(
                created__gte=from_date, created__lte=to_date).count()})
        result["week_statistics"] = week_statistics
        return response.Response(result)


class InsuranceFormViewSet(viewsets.ModelViewSet):
    """ViewSet for the Insurance Form class"""

    queryset = models.InsuranceForm.objects.all()
    serializer_class = serializers.InsuranceFormSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = [permissions.IsAuthenticated, HasGroupRolePermission]


class InsuranceFormUploadViewSet(viewsets.ModelViewSet):
    """ViewSet for the Insurance Form Upload class"""

    queryset = models.InsuranceFormUpload.objects.all()
    serializer_class = serializers.InsuranceFormUploadSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = [permissions.IsAuthenticated, HasGroupRolePermission]

    def create(self, request, *args, **kwargs):
        data = request.data

        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


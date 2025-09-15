from django.http import JsonResponse
from myapp.models import Employee

def employee_list(request):
    qs = Employee.objects.all().values('name','email','department')
    return JsonResponse(list(qs), safe=False)


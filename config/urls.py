from django.contrib import admin
from django.urls import path
from myapp.views import employee_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee_list/', employee_list),
]


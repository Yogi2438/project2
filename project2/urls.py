from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('Login/',views.studlogin,name='studlogin'),
    path('chklogin/',views.chklogin,name='chklogin'),
]

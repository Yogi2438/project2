from django.shortcuts import render
from django.http import HttpResponse
from .forms import fregister
from .models import mregister
# Create your views here.

def home(request):
	studdata={'studregform':fregister}
	return render(request,'student/home.html',studdata)

def addstudent(request):
	Name=request.POST.get('name')
	Roll_no=request.POST.get('roll_no')
	Std=request.POST.get('std')
	Email=request.POST.get('email')
	Phone=request.POST.get('phone')
	mregister.objects.create(name=Name,roll_no=Roll_no,std=Std,email=Email,phone=Phone)
	Sdata=mregister.objects.all()
	StudDataDic={'StudData':Name,'StudAllData':Sdata}
	return render(request,'student/login.html',StudDataDic)

def studlogin(request):
	return render(request,'student/StudentLogin.html')

def chklogin(request):
	if request.method == 'POST':
		LoginData = mregister.objects.all()
		# Two way off get data in variable 1st way
		# temail=request.POST.get('txtemail')
		# tphone=request.POST.get('txtphone')
		# 2nd way
		femail=request.POST['txtemail']
		fphone=request.POST['txtphone'] #direct request.objects you write in condition
		
		# memail=mregister.objects.get('email')
		# mphone=mregister.objects.get('phone')
		print(femail)
		if mregister.objects.filter(email=femail,phone=request.POST['txtphone']):
			Ldata={'LoginData':LoginData,'msg':'Successfull Login Your Wellcom...'}
			return render(request,'student/demo.html',Ldata)
		else:
			return HttpResponse("Not valid user")
	else:
		return HttpResponse("Not valid Request")
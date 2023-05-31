from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def team_form(request):
    tp=input('enter the value : ')
    ob=cricket.objects.get_or_create(Team=tp)[0]
    ob.save()
    return HttpResponse('insert data success') 

def detail_form(request):
    tp=input('enter the team : ')
    na=input('enter the name : ')
    ag=int(input('enter the age : '))
    em=input('enter the email : ')

    ob=cricket.objects.get_or_create(Team=tp)[0]
    ob.save()
    dp=detial.objects.get_or_create(Team=ob,Name=na,Age=ag,Email=em)[0]
    dp.save()
    return HttpResponse('insert data successfully')

def access_form(request):
    na=input('enter the name : ')
    wf=input('enter the wifename : ')
    cd=int(input('enter the number of child : '))
    dp=detial.objects.get_or_create(Name=na)[0]
    dp.save()
    ad=access.objects.get_or_create(Name=dp,Wife=wf,Child=cd)[0]
    ad.save()
    return HttpResponse('insert data successfully')

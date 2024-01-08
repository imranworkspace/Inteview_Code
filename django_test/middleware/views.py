from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def myview(request):
    print('inside view')
    return HttpResponse('please check your logs')
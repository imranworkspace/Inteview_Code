from django.shortcuts import render

# Create your views here.
def mystat(request):
    return render(request,'mystat/index.html')
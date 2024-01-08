from django.shortcuts import render
from datetime import datetime,timedelta
# Create your views here.
def set_cookie(request):
    response = render(request,'stud/set.html')
    # response.set_cookie('name','imran',expires=datetime.utcnow()+timedelta(milliseconds=30))
    response.set_cookie('name','imran',expires=datetime.utcnow()+timedelta(minutes=1))
    # response.set_cookie('name','imran',expires=datetime.utcnow()+timedelta(days=2))
    return response
    
def get_cookie(request):
    name=request.COOKIES.get('name','guest')
    return render(request,'stud/get.html',{'nm':name})

def del_cookie(request):
    response = render(request,'stud/del.html')
    response.delete_cookie('name')
    return response
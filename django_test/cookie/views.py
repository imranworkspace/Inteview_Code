from django.shortcuts import render
# Create your views here.
def set_cookie(request):
    response = render(request,'stud/set.html')
    response.set_cookie('name','imran',max_age=60)
    return response
    
def get_cookie(request):
    name=request.COOKIES.get('name','guest')
    return render(request,'stud/get.html',{'nm':name})

def del_cookie(request):
    response = render(request,'stud/del.html')
    response.delete_cookie('name')
    return response
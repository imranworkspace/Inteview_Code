from django.shortcuts import render

# Create your views here.
def home(request):
    context={
        'name':'imran'
    }
    return render(request,'index.html',context)
    # return render(request,'index.html',context,content_type='application/xhtml/xml') # if you want to download this file use content_type
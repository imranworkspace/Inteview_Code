from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    context={
        'name':'imran',
        'dt':datetime.now()
        
    }
    return render(request,'index.html',context)
    # return render(request,'index.html',context,content_type='application/xhtml/xml') # if you want to download this file use content_type
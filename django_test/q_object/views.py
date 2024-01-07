from .models import StudentModel
from django.db.models import Q
import json
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

def q_obj(request):
    # obj=StudentModel.objects.filter(Q(name__startswith='i'), Q(lname__startswith='s')| Q(lname__startswith='p'))
    obj=StudentModel.objects.filter(Q(lname__startswith='p'))
    # Convert the QuerySet to a list of dictionaries
    data = list(obj.values())
    # Serialize the list to JSON
    serialized_data = json.dumps(data, cls=DjangoJSONEncoder, indent=2)
    return JsonResponse({'data': serialized_data}, safe=False)
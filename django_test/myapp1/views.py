from django.shortcuts import render
from .models import StudentModel
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
# Create your views here.
def create(request):
    try:
        # student=StudentModel.objects.get(id=1)
        # student.city='Lonavala'
        # student.save()

        # student=StudentModel.objects.get(id=3)
        # student.delete()

        student=StudentModel.objects.get(id=5)

        student_dict = model_to_dict(student)
        # Serialize the dictionary to JSON
        serialized_data = JsonResponse(student_dict, safe=False)
        return serialized_data
    except StudentModel.DoesNotExist:
        return JsonResponse({'msg':'record not found'})
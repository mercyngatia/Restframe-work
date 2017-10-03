from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer


# Create your views here.
def welcome (request):
    return render(request, 'Listing_students.html')
def students(request):
    students = Student.objects.all()
    context ={
        'students': students
    }
    return render(request,'listing_students.html', context)
    
#ViewSets define the view behavior

class StudentViewSet(viewsets.ModelViewSet):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer


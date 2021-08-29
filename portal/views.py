from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def say_hello(request):
    x = 1
    return render(request, 'hello.html', { 'name': 'axl' })

# home
def index(request):
    students = Student.objects.all().order_by('name')
    courses = Course.objects.all().order_by('name')

    context = {
        'students': students,
        'courses': courses,
    }
    return render(request, 'index.html', context=context)

# course detail
def course(request, course_id):
    course = Course.objects.get(pk=course_id)
    course_members = CourseMember.objects.all().filter(course_id__exact=course_id)#.order_by('student.name')

    context = {
        'course': course,
        'course_members': course_members,
    }
    return render(request, 'course.html', context=context)

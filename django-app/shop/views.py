from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course

# !!!! CONTROLLER FILE


def index(request):
    courses = Course.objects.all()
    return render(request, 'shop/courses.html', {'courses': courses})


def single_course(request, course_id):
    # Option 1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'shop/single-course.html',  {'course': course})
    # except Course.DoesNotExist:
    #     raise Http404()
    
    # Option 2
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/single-course.html',  {'course': course})


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course
from .forms import ContactForm


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

def single_course_edit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            title = form.cleaned_data[course.title]
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            # ...
    else:
        form = ContactForm()
    return render(request, 'shop/single-course-edit.html',  {'course': course, 'form': form})



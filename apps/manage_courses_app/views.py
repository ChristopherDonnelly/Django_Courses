from __future__ import unicode_literals 
 
from django.shortcuts import render, HttpResponse, redirect 
from django.utils.html import escape
from django.contrib import messages
from .models import Course
 
def index(request):
    print Course.objects.all()
    return render(request, "manage_courses_app/index.html", { 'courses': Course.objects.all() }) 

def new(request):
    return render(request, "manage_courses_app/new.html")


def create(request):
    errors = Course.objects.basic_validator(request.POST)
    goto = '/'

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)

        request.session['name'] = request.POST['name']
        request.session['desc'] = request.POST['desc']

    else:
        try:
            Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])

            del request.session['name']
            del request.session['desc']
        except:
            pass

    return redirect(goto)

def destroy(request, course_num):
    exists = Course.objects.filter(id=course_num).count()
    if exists:
        Course.objects.get(id=course_num).delete()
    return redirect('/')

def comment(request, course_num):
    return redirect('/')

def delete(request, course_num):
    return render(request, "manage_courses_app/delete.html", { 'course': Course.objects.get(id=course_num) })
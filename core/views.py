from django.shortcuts import render
from core.models import *
from django.http import HttpResponseRedirect

def index(request):
    projects = Project.objects.filter(current=True)
    work = Experience.objects.filter(type='WORK')
    education = Experience.objects.filter(type='EDUCATION')
    courses = Experience.objects.filter(type='COURSE')
    key_skills = KeySkill.objects.filter(current=True)
    
    context = {
        'projects': projects,
        'work': work,
        'education': education,
        'courses': courses,
        'key_skills': key_skills,
    }
    return render(request, 'core/index.html', context)

def githb(request):
    return HttpResponseRedirect("https://github.com/whyspark")


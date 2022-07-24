from http.client import responses
from django.shortcuts import render
from core.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from smtplib import SMTPException
from django.utils.html import strip_tags

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

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

def send_email(request):
    error = {}
    name = request.POST.get('contactName', '')
    subject = request.POST.get('contactSubject', '')
    contact_message = request.POST.get('contactMessage', '')
    from_email = request.POST.get('contactEmail', '')
    
    if len(name) < 2:
        error['name'] = 'Please enter your name.'
        
    try:
        validate_email(from_email)
    except ValidationError:
        error['email'] = f'Please enter a valid email address.'

    if len(contact_message) < 15:
        error['message'] = 'Please enter your message. It should have at least 15 characters.'
    
    if subject == '':
        subject = 'lukepomeroy.co.uk Contact Form Submissions'

    if len(error) > 0:
        response = 'Your submission has the following errors: <br />'
        for err in error:
            response += f'{error[err]} <br />'
        return HttpResponse(response)
    
    message = f'Email from: {name} <br />'
    message += f'Email address: {from_email} <br />'
    message += f'Message: <br />'
    message += contact_message
    message += '<br /> ----- <br /> This email was sent from the contact form on lukepomeroy.co.uk. <br />'
    plain_message = strip_tags(message)

    if subject and message and from_email:
        try:
            send_mail(subject, plain_message, None, ['lukepomeroy@hotmail.co.uk'], html_message=message)
        except BadHeaderError:
            return HttpResponse('Your submission contains bad headers!')
        except SMTPException as e:
            return HttpResponse(f'There was an error sending an email. <br />{e}')
        return HttpResponse('OK')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')
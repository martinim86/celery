# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from .send import send_email
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils import timezone
from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.template import Context

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf.global_settings import DEFAULT_FROM_EMAIL
RECIPIENTS_EMAIL = ['manager@mysite.com']

def contacts_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            data = {
                "name": form.cleaned_data['subject'],
                "surname": "Mustang",
                "email": form.cleaned_data['from_email'],
            }
            try:
                # send_mail(subject, message,
                #           DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
                # print('fi')
                subject = "Тема для вашего письма"
                current_context = Context({'username': 'User1'})
                # text_content = get_template('email.txt').render(current_context)
                html_content = render_to_string('send.html', data)
                from_email = 'yourfromemail'
                # msg = EmailMultiAlternatives(subject, message, from_email, RECIPIENTS_EMAIL)
                # msg.attach_alternative(html_content, "text/html")
                # res = msg.send()
                send_email.delay(RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, 'email.html', {'form': form})

def success_view(request):
    print('RECIPIENTS_EMAIL')
    return HttpResponse('Приняли! Спасибо за вашу заявку.')

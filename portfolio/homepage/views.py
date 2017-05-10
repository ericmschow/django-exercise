from django.template.response import TemplateResponse
from django import forms
from django import http
from homepage import forms
from django.core.mail import send_mail
from django.core.mail import EmailMessage
# class NameForm (forms.Form):
#     your_name = forms.CharField(label="Your name", max_length=10)

def homepage (request):
    context = {
    'page_title': 'home page',
    'numbers': [1, 2, 3, 4]
    }
    return TemplateResponse(request, 'homepage.html', context)

def thanks(request):
    context = {}
    return TemplateResponse(request, 'thanks.html', context)

def contact (request):
    form = forms.emailForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = EmailMessage()
            email.subject = form.cleaned_data['name']
            email.body = form.cleaned_data['message']
            email.from_email = form.cleaned_data['email']
            email.to = ['eric.m.schow@gmail.com']

            email.attach_file(form.cleaned_data['attachment'])
            email.send()
            return http.HttpResponseRedirect('/thanks/')
        else:
            print(form.errors)


    context = {}
    return TemplateResponse(request, 'contact.html', context)

# def hello (request):
#     form = NameForm(request.POST or None)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             print(form.cleaned_data['your_name'])
#             send_email()
#             return http.HttpResponseRedirect('/thanks/')
#
#     context = {
#         'form': form,
#     }
#     return TemplateResponse(request, 'hello.html', context)

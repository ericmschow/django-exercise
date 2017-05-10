from django import forms

class emailForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    message = forms.CharField(label='message', max_length=500)
    attachment = forms.FileField(label='attachment')

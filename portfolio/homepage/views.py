from django.template.response import TemplateResponse

def homepage (request):
    context = {
    'page_title': 'home page',
    'numbers': [1, 2, 3, 4]
    }
    return TemplateResponse(request, 'homepage.html', context)

def contact (request):
    context = {}
    return TemplateResponse(request, 'contact.html', context)

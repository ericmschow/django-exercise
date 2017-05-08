from django.template.response import TemplateResponse

def experiment (request):
    context = {}
    return TemplateResponse(request, 'experiment.html', context)

def medium (request):
    context = {}
    return TemplateResponse(request, 'medium.html', context)

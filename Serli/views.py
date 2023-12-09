from django.http import HttpResponse
from django.template import loader

def Serli(request):
  template = loader.get_template('artika.html')
  return HttpResponse(template.render())
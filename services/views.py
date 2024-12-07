from django.shortcuts import render
from .models import Service
# Create your views here.
def service(request,**kwargs):
    if kwargs.get('category'):
        service = Service.objects.filter(category__title=kwargs.get('category'))    
    context = {
        'services':service
    }
    return render(request,'service/services.html',context=context)
   
    
def service_detail(request):
    id = request.GET.get('id')
    service = Service.objects.get(id=id)
    context = {
        'services':service
    }
    return render(request,'service/service-details.html',context=context)

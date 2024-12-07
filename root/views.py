from django.shortcuts import render
from .models import tester,score
# Create your views here.
def home(request):
    scors = score.objects.all()
    testers = tester.objects.all()
    context = {
        'testers':testers
    }
    return render(request,'root/index.html',context=context)
def agent(request):
    return render(request,'root/agents.html')
def about(request):
    return render(request,'root/about.html')
def contact(request):
    return render(request,'root/contact.html')

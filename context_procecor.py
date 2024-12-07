from root.models import ctaegory

def jeneral(request):
    category =  ctaegory.objects.all()
    context = {
        'categorys' : category
    }
    return context
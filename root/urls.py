from django.urls import path
from .views import home,agent,about,contact
urlpatterns = [
    path('',home),
    path('agent',agent),
    path('about',about),
    path('contact',contact)
]
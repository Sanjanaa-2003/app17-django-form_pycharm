from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),   #implies that the home page should be connected to this function; In flask, decorators are used for this purpose
    path('about/', views.about, name='about')
]




# Open terminal and run the following:
#     python manage.py runserver
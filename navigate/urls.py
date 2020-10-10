from . import views
from django.urls import path
from django.contrib import admin
urlpatterns =[
    
    path('',views.index,name='index'),
   
    path('analyze',views.analyze,name='analyze'),
    

]

from django.urls import path , include
from . import views

urlpatterns = [
    
    path('', views.index , name= 'index'),
  
    path('appointment/',views.appointment , name= 'appointment'),
    path('blog/',views.blog ,name= 'blog'),
    path('contact/',views.contact , name='contact'),
    path('price/',views.price , name='price'),
  
  
    path('testmonial/',views.testmonial , name='testmonial'), 
    path('team/',views.team , name='team'),
    path('departments/',views.departments , name= 'departments'),
  
]
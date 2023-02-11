from django.shortcuts import render
from django.db.models import Q
from. models import Department , Team
from . forms import BookingForm, messagform
# Create your views here.

def index(request):
    return render(request, 'index.html')



def appointment(request):

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
               form.save() 
               return render (request, 'sucs.html')

    form = BookingForm()
    dict_form={
        'form': form

    }

    return render(request, 'appointment.html', dict_form)

def blog(request):
    return render(request, 'blog.html')


def contact(request):

    if request.method == "POST":
        form =messagform(request.POST)
        if form.is_valid():
               form.save() 
               return render (request, 'msgsuc.html')

    forms = messagform()
    dict_form={
        'form': forms

    }

    return render(request, 'contact.html', dict_form)

   

def price(request):
    return render(request, 'price.html') 


def team(request):

    dict_doc={
        'doc':Team.objects.all()
    }


    return render(request, 'team.html', dict_doc)

    
def testmonial(request):
    return render(request, 'testmonial.html') 
 
def departments(request):
 
    dict_dept={
        'dept':Department.objects.all()
     }
    return render(request, 'departments.html', dict_dept) 

    

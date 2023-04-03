from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def  IndexView(request): # Index.html View
    return render( request, "app/index.html")


def show(request):
    return render(request, "app/show.html")

def Forms(request):
    if request.method=='POST':
    #data come from html to view
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        contact = request.POST['contact']
    
    #creating object of model class.
    #inserting data into table
        newuser = student.objects.create(Firstname = first, Lastname = last, Email = email, Contact = contact)
        newuser.save()
        return redirect('show')
    #after insert render on show view
    else:
        return render(request, "app/Forms.html")
    
    
def show(request):
    #select * from tablename
    # for fetching all the data of the table
    all_data = student.objects.all()
    return render(request, "app/show.html", {'key1':all_data})
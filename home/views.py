from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact

# Create your views here.

def home(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        print(fname, lname, email, phone , msg)
        newContact = Contact(fname=fname,lname=lname, email=email, phone=phone, msg=msg)
        newContact.save()
        return HttpResponse("Contact Saved!")
    else:
        return HttpResponse("Contact Page")


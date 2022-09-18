from django.contrib import messages
from django.shortcuts import render,HttpResponse
from home.models import Contact
def index(request):
    context = {
        'variable1':"i am from mars",
        'variable2':"i am from titan"
    }
    return render(request,'index.html',context)
# Create your views here.
def about(request):
    return render(request,'about.html')
def sevices(request):
    return render(request,'services.html')
def contact(request):
    if(request.method=='POST'):
        name  = request.POST.get('name')
        email  = request.POST.get('email')
        phone  = request.POST.get('phone')
        desc  = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, 'Your Quieries has been send')
    return render(request,'contact.html')
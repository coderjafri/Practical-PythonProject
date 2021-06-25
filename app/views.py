from django.contrib import messages
from django.shortcuts import redirect, render
from  django.http import JsonResponse
from app.models import contarct
import json

# Create your views here.

def index(req):
 if req.method=="POST" : 
     name=req.POST['name']
     email=req.POST['email']
     phone=req.POST['phone']
     msg=req.POST['msg']
     data=contarct(name=name,email=email,phone=phone,msg=msg)
     data.save()
     redirect('/')
     messages.success(req, 'Form submission successful')
 show=contarct.objects.all()
 content={
     "show":show
 }
 return render(req, 'home.html' ,content)

def contact(req):
    json_data = open('data/file.json')  
    data1 = json.loads(json_data.read()) # deserialises it
    data2 = json.dumps(data1) # json formatted string
    json_data.close()
    content={
     "data2":data2
 }
    
    return render(req, 'jsondata.html' ,content)

def about(req):
    return render(req, 'about.html')




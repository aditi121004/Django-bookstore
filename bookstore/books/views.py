from django.shortcuts import render

# Create your views here. 

def index(req):
    return render(req,'index.html')
def signup(req):
    return render(req,'signup.html')
def signin(req):
    return render(req, 'signin.html')
def about(req):
    return render(req,'about.html')
def contact(req):
    return render(req,'contact.html')

from datetime import datetime
def DTLdemo(req):
    name='vedant'
    crtdatetime=datetime.now()
    greetings="Goodmorning"
    password= "admin"
    authors=['pp','jj', 'cc']
    students={1001:{'name':'aditi','issuedbook':'python'},
              1002:{'name':'raaj','issuedbook':'java'}}
    curhour= datetime.now().hour
    context={
             'name':name, 
             'crtdatetime':crtdatetime, 
             'greetings':greetings, 
             'password':password, 
             'curhour':curhour, 
             'authors': authors,
             'students':students,
             }
    return render(req,'DTLdemo.html',context)

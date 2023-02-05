from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from .models import orderTable
# Create your views here.


def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pswd=request.POST['pswd']
        user=auth.authenticate(username=uname,password=pswd)
        if user is not None:
            auth.login(request,user)
            print('reggusred')
            return redirect('home')
        else:
            messages.info(request,'invalid credentials!!')    
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pswd=request.POST['pswd']
        cpswd=request.POST['cpswd']
       
        if pswd != cpswd:
            messages.info(request,'password didnt match!!')
        else:
            check=User.objects.filter(username=uname).exists()
            if check:
                messages.info(request,'username taken already!!')   
            else:
                reg=User.objects.create_user(username=uname,password=pswd)
       
                reg.save()
                
                return redirect('login')
                
            
                    
    return render(request,'register.html')  


def home(request):
    return render(request,'home.html')
      

def logout(request):
    auth.logout(request)
    return redirect('home') 


def orderItem(request):
    courses=['Computer science','Physics','BBA','Bcom','Malayalam','Hindi','Others']
    if request.method=='POST':
        name=request.POST['name']
        dob=request.POST['dob']
        age=request.POST['age']
        gender=request.POST['gender']
        mobile=request.POST['Phone']
        email=request.POST['email']
        address=request.POST['address']
        dptmnt=request.POST['parent']
        course=int(request.POST['child'])
        purpose=request.POST['purpose']
        materials=request.POST.getlist('checks[]')
     
        course=courses[course+1]
       
        data = orderTable.objects.create(name=name,
        dob=dob,
        age=age,
        gender=gender,
        mobile=mobile,
        email=email,
        address=address,
        dptmnt=dptmnt,
        course=course,
        purpose=purpose,
        materials=materials
        )
        data.save()
        return render(request,'conform.html')

       

    return render(request,'form.html')    
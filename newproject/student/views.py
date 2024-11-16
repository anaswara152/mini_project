import datetime
from turtle import update
from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib import messages
from librarian.models import book

from .models import*
from django.http import JsonResponse
# Create your views here.


def registration(request):
        if  request.method == 'POST':
                name=request.POST['name']
                age=request.POST['age']
                gender=request.POST['gender']
                if gender:
                      print('selected')
                else:
                      print('not selected')
              
                address=request.POST['address']
                username=request.POST['username']
                password=request.POST['password']
                if len(request.FILES)>0:
                     img=request.FILES['file']
                else:
                  img="no pic"
                m=student.objects.create(name=name,age=age,gender=gender,address=address,username=username,password=password,profilephoto=img)
                m.save()
                messages.info(request,'registration is sucessfull')
        return render(request,"student/register.html")


def get_username(request):
      user=request.GET['us']
      data=student.objects.filter(username=user)
      if data.count()>0:
            msg="exist"
      else:
            msg="not exist"
      return JsonResponse({'valid':msg})


def studenthome(request):
     return render(request,'student/studenthome.html')
def viewbooks(request):
      m=book.objects.all()
      p={'m':m}
      return render(request,'student/displaybook.html',p)
      
def bookingbook(request,id):
      book1=book.objects.filter(id=id)
      studentid=request.session['id']
      date=datetime.datetime.now()
      number=book1[0].numberof_copies
      if number==0:
            messages.info(request,'can not get the book')   
            return redirect('viewbooks')
      else:
            ab=booking.objects.create(bookid_id=id,studentid_id=studentid,booking_date=date,return_date="null")   
            ab.save()
            quantity=number-1
            p=book1.update(numberof_copies=quantity)
      return redirect('viewbooks')

def bookdeatils(request):
      std=request.session['id']
      ab=booking.objects.filter(studentid_id=std)
      s={'m':ab}
      return render(request,'student/displaydeatils.html',s)

def reservedbook(request):
      std=request.session['id']
      n=booking.objects.filter(studentid_id=std,status='pending')
      d={'n':n}
      return render(request,'student/reservedbook.html',d)

def returnbook(request,id):
      date=datetime.datetime.now()
      b=booking.objects.filter(id=id).update(status="returned")
      bookin_date=date
      return redirect('reservedbook')

def logout(request):
      if 'id' in request.session:
           request.session.flush()
      return redirect('login')
def newpassword(request):
      if request.method=="POST":
            old_password=request.POST['old_password']
            new_password=request.POST['new_password']
            confirm_password=request.POST['confirm_password']
            if new_password==confirm_password:
                  data=student.objects.filter(password=old_password)
                  if data.count()>0:
                        n=student.objects.filter(id=data[0].id).update(password=new_password)
                        messages.info(request,'password changed')
            else:
                  messages.info(request,'incorrect password')
                  return redirect('reservedbook')
      return render(request,'student/newpassword.html')   
def viewprofile(request):
      ab=student.objects.filter(id=request.session['id'])  
      h={'m':ab}  
      return render(request,'student/viewprofile.html',h) 
def forgot(request):
      if request.method=='POST':
            username=request.POST['username']
            data=student.objects.filter(username=username)
            if data.count()>0:
                  request.session["newid"]=data[0].id
                  messages.info(request,'username is found')
                  return redirect('newform')
            
            else:
                  messages.error(request,'username is not found')
            
      return render(request,'student/forgot.html')

def newform(request):
      if request.method=="POST":
            name=request.POST['name']
            age=request.POST['age']
            address=request.POST['address']
            m=student.objects.filter(name=name,age=age,address=address)
            if m.count()>0:
                  return redirect('finalpage')
            else:
                  messages.info(request,'details are not correct')
      return render(request,'student/newform.html')

def finalpage(request):
      if request.method=="POST":
           id=request.session["newid"]
           new_password=request.POST['new_password']
           m=student.objects.filter(id=id).update(password=new_password)
           messages.info(request,'password updated sucessfully')

      return render(request,'student/finalpage.html')



      



      
      
      
      






    




from turtle import update
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib import messages

from student.models import booking, student
from .models import*
# Create your views here

def login(request):
    if 'id' in request.session and 'role' in request.session:
         if request.session['role']=='librarian':
              return redirect('adminhome')
         elif 'id' in request.session and 'role' in request.session:
              return redirect('studenthome')
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        admin=library.objects.filter(username=username,password=password).first()
        student1=student.objects.filter(username=username,password=password).first()
        if admin:
            request.session['id']=admin.id
            request.session['role']='librarian'
            return redirect('adminhome')
        elif student1:
            request.session['id']=student1.id
            request.session['role']='student'

            return redirect('studenthome')        
        else:
              messages.error(request,'invalid credential')

    return render(request,'login.html') 

def home(request):
     if 'id' in request.session and 'role' in request.session:
         if request.session['role']=='librarian':
              return redirect('adminhome')
         elif 'id' in request.session and 'role' in request.session:
              return redirect('studenthome')
     m=book.objects.all()
     p={'m':m}
     return render(request,'home.html',p) 

def adminhome(request):
     return render(request,'admin/adminhome.html')

def logout(request):
      if 'id' in request.session:
           request.session.flush()
      return redirect('login')

def addcategory(request):
     if request.method == 'POST':
          p=request.POST['category']
          m=category.objects.create(name=p)
          m.save()
          messages.info(request,'data added sucessfully')

     return render(request,'admin/category.html')

def addbook1(request):
     m=category.objects.all()
     if request.method == "POST":
          name=request.POST['name']
          author=request.POST['author']
          numberof_copies=request.POST['numberof_copies']
          categoryid=request.POST['category']
          if len(request.FILES)>0:
               img=request.FILES['file']
          else:
               img="no pic"   
          
          p=book.objects.create(name=name,author=author,coverphoto=img,numberof_copies=numberof_copies,categoryid_id=categoryid)
          p.save()
          messages.info(request,' book added sucessfully')
     s={'m':m}
     return render(request,'admin/addbook.html',s)     
  
def viewbook(request):
     m=book.objects.all()
     p={'m':m}
     return render(request,'admin/display.html',p)

def delete(request,id):
    u=book.objects.filter(id=id).delete()
    return redirect('viewbook')   





def edit(request,id):
     u=get_object_or_404(book,id=id)
     m=category.objects.all()
     if request.method=="POST":
          name=request.POST['name']
          author=request.POST['author']
          numberof_copies=request.POST['numberof_copies']
          categoryid=request.POST['category']
          if len(request.FILES)>0:
               img=request.FILES['file']
          else:
               img="no pic"    
          u.name=name
          u.author=author
          u.coverphoto=img
          u.numberof_copies=numberof_copies
          u.categoryid_id=categoryid
          u.save()
          messages.info(request,"updated sucessfully")
          return redirect('viewbook')
     u=book.objects.filter(id=id) 
     y={'u':u,'m':m}
     return render(request,'admin/edit.html',y)

def librarianview(request):
     a=booking.objects.all()
     s={'a':a}
     return render(request,'admin/librarianview.html',s)

def returnbookview(request):
     b=booking.objects.filter(status="returned")
     s={'b':b}
     return render(request,'admin/returnbookview.html',s)

def acceptbook(request,id):
     abc=get_object_or_404(booking,id=id)
     abc.status='accepted'
     abc.save()
     books=get_object_or_404(book,id=abc.bookid_id)
     copies=books.numberof_copies
     books.numberof_copies=copies+1
     books.save()
     return redirect('returnbookview')

def password(request):
     if request.method=="POST":
          old_password=request.POST['old_password']
          new_password=request.POST['new_password']
          confirm_password=request.POST['confirm_password']
          if new_password==confirm_password:
               data=library.objects.filter(password=old_password)
               if data.count()>0:
                    m=library.objects.filter(id=data[0].id).update(password=new_password)
                    messages.info(request,'password changed succefully')

          else:
             messages.info(request,'password incorrect')
             return redirect('returnbookview')
     return render(request,'admin/password.html')
     
          
     







     


     







     
     



     




     
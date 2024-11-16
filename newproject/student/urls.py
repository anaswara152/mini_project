
from django.urls import path
from student import views
urlpatterns = [

    path('registration',views.registration,name='registration'),
    path('studenthome',views.studenthome,name="studenthome"),
    path('viewbooks',views.viewbooks,name="viewbooks"),
    path('bookingbook/<int:id>',views.bookingbook,name="bookingbook"),
    path('bookdeatils',views.bookdeatils,name="bookdeatils"),
    path('reservedbook',views.reservedbook,name="reservedbook"),
    path('returnbook/<int:id>',views.returnbook,name="returnbook"),
    path('logout',views.logout,name="logout"),
    path('newpassword',views.newpassword,name="newpassword"),
    path('viewprofile',views.viewprofile,name="viewprofile"),
    path('forgot',views.forgot,name="forgot"),
    path('newform',views.newform,name="newform"),
    path('finalpage',views.finalpage,name="finalpage"),
    path('get_username',views.get_username,name="get_username")

    
]


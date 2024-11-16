
from django.urls import path
from librarian import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('logout',views.logout,name="logout"),
    path('addcategory',views.addcategory,name="addcategory"),
    path('addbook1',views.addbook1,name="addbook1"),
    path('viewbook',views.viewbook,name="viewbook"),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('librarianview',views.librarianview,name="librarianview"),
    path('returnbookview',views.returnbookview,name="returnbookview"),
    path('acceptbook/<int:id>',views.acceptbook,name="acceptbook"),
    path('password',views.password,name="password"),
    # path('edit_action',views.edit_action,name='edit_action'),

    
]


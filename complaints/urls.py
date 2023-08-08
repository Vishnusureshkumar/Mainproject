from django.urls import path
from complaints.views import About,Home,Contact,Logout_staff,Useri,regcomplaints,Viewstatcomplaints,Feedcomplaints,Staffdash,Viewcomplaints,Logout_user,Index,Login_govt,Addstaff,Adduser,Addservice
from .import views 



urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('logout_admin/', views.logout_admin, name='logout_admin'),
    path('index/', Index, name='index'),
    path('adduser/', Adduser, name='adduser'),
    path('useri/', Useri, name='useri'),
    path('regcomplaints/', regcomplaints, name='regcomplaints'),
    path('viewstatcomplaints/', Viewstatcomplaints, name='viewstatcomplaints'),
    path('feedcomplaints/', Feedcomplaints, name='feedcomplaints'),
    path('staffdash/', Staffdash, name='staffdash'),
    path('viewcomplaints/', Viewcomplaints, name='viewcomplaints'),
    path('user/signup/',views.SignupPage, name='signup'),
    path('user/logi/',views.LoginPage, name='logi'),
    path('logout_user/', Logout_user, name='logout_user'),
    path('logout_staff/', Logout_staff, name='logout_staff'),
    path('loggvt/', views.Login_govt, name='loggvt'),
    path('addstaff/', Addstaff, name='addstaff'),
    path('addservice/', Addservice, name='addservice'),
    path('adduser/', Adduser, name='adduser'),
    path('managestaff/', views.Managestaff, name='managestaff'),
    path('manageuser/', views.Manageuser, name='manageuser'),
    path('viewcomp/', views.Viewcomp, name='viewcomp'),
    path('viewstatus/', views.viewstatuses, name='viewstatuses'),
    path('adduseri/', views.Adduseri, name='adduseri'),
    path('viewcomplaints/', views.Viewcomplaints, name='viewcomplaints'),
    # path('delete_user/', views.delete_user, name='delete_user'),
]


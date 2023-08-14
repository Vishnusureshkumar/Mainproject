from django.urls import path
from complaints.views import About,Home,Contact,Logout_staff,Useri,regcomplaints,Viewstatcomplaints,Feedcomplaints,Staffdash,Viewcomplaints,Logout_user,Index,Addstaff,Adduser,Addservice
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
    path('staffi/', views.Staffi, name='staffi'),
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
    path('manageuseri/', views.Manageuseri, name='manageuseri'),
    path('viewcomp/', views.Viewcomp, name='viewcomp'),
    path('viewstatus/', views.viewstatus, name='viewstatuses'),
    path('adduseri/', views.Adduseri, name='adduseri'),
    path('viewcomplaints/', views.viewcomplaints, name='viewcomplaints'),
    path('viewplum/', views.viewplum, name='viewplum'),
    path('viewcon/', views.viewcon, name='viewcon'),
    path('viewother/', views.viewother, name='viewother'),
    path('con_staff/', views.con_staff, name='con_staff'),
    path('elec_staff/', views.elec_staff, name='elec_staff'),
    path('plum_staff/', views.plum_staff, name='plum_staff'),
    path('other_staff/', views.other_staff, name='other_staff'),
    path('con_delete_user<int:id>/', views.con_delete_user, name='con_delete_user'),
    path('plum_delete_user<int:id>/', views.plum_delete_user, name='plum_delete_user'),
    path('elec_delete_user<int:id>/', views.elec_delete_user, name='elec_delete_user'),
    path('other_delete_user<int:id>/', views.other_delete_user, name='other_delete_user'),
    #path('delete_user/<id>', views.delete_user, name='delete_user'),
    path('viewfeedback/', views.Viewfeedback, name='viewfeedback'),
    path('admin_delete_user/<int:id>',views.admin_delete_user,name='admin_delete_user'),
    path('staff_delete_user/<int:id>',views.staff_delete_user,name='staff_delete_user'),
    #path('send_email/', views.send_email, name='send_email'),
    path('contactus/', views.Contactus, name='contactus'),
    path('admin_update/<id>/',views.admin_update,name='admin_update'),
    path('admin_delete_comp/<id>/',views.admin_delete_comp,name='admin_delete_comp'),
    path('staff_update_comp/<id>/',views.staff_update_comp,name='staff_update_comp'),



]


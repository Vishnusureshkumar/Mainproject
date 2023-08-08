from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages,auth
from .forms import NewUserForm

from .models import *
# Create your views here.
def About(request):
    return render(request,'about.html')

def Home(request):
    return render(request,'home.html')


def Contact(request):
    return render(request,'contact.html')


def Useri(request):

    if 'username' in request.session:
        username = request.session['username']
        # Use the username as needed in your view logic
    # else:
    #     # Handle the case when the username is not in the session
    #     pass
    return render(request,'useri.html')

def regcomplaints(request):  # sourcery skip: extract-method
    username = request.session['username']
    if request.method == "POST":
        data = request.POST
        name=username
        flatblock=data.get('flatblock')
        flatno=data.get('flatno')
        date=data.get('date')
        email=data.get('email')
        phoneno=data.get('phoneno')
        complainttitle=data.get('complainttitle')
        complaintdescription=data.get('complaintdescription')
        complaintmedia=request.FILES.get('complaintmedia')
        
        Regcomplaint.objects.create(
            name=name,
            flatblock=flatblock,
            flatno=flatno,
            date=date,
            email=email,
            phoneno=phoneno,
            complainttitle=complainttitle,
            complaintdescription=complaintdescription,
            complaintmedia=complaintmedia,
        )
        return redirect('/regcomplaints/')
    queryset =Regcomplaint.objects.all()
    context ={'regcomplaints':queryset}  
    
    return render(request,'regcomplaints.html',context)

def Viewstatcomplaints(request):
    username=request.session['username']
    queryset =Regcomplaint.objects.filter(name= username)
    context ={'regcomplaints':queryset}  
    
    return render(request,'viewstatcomplaints.html',context)

def Feedcomplaints(request):
    if request.method == "POST":
        feed_sub = request.POST['feed_sub']
        feed_description = request.POST['feed_description']
        Feedback.objects.create(feed_sub=feed_sub,
                                     feed_description=feed_description, 
                                    )  
        Feedback(feed_sub=feed_sub, feed_description=feed_description)
        messages.info(request,'Successfully Added your Feedback')
        return redirect('feedcomplaints')
    return render(request,'feedcomplaints.html')

def Staffdash(request):
    return render(request,'staffdash.html')
def Viewcomplaints(request):
    return render(request,'viewcomplaints.html')  

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

def Adduser(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"signup Successfull.")
            return redirect('adduser')
        else:
            messages.error(request,"unsuccessfull registration.invalid information")
    form = NewUserForm()
    return render(request=request, template_name="admin/adduser.html", context={"register_form":form})
        
   
        
    

def admin_login(request):
    error = ""
    if request.method == "POST":
        u =request.POST['uname']
        p =request.POST['pwd']
        user =auth.authenticate(username=u, password=p)
        try  :
            if user.is_staff:
                login(request,user)
                error ="no"
            else:
                error="yes"
        except Exception:
            error="yes"
    d={'error':error}
    return render(request,'login.html',d)

def logout_admin(request):
    logout(request)
    return redirect('admin_login')

# def logout_admin(request):
    
#     logout(request)
#     return redirect('Login')




#user reg
def SignupPage(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"signup Successfull.")
            return redirect('logi')
    messages.error(request,"unsuccessfull registration.invalid information")
    form = NewUserForm()
    return render(request=request, template_name="user/signup.html", context={"register_form":form})
        
	
    #if request.method == "POST":
#        uname=request.POST.get('username')
#        email=request.POST.get('email')
#        pass1=request.POST.get('password1')
#        pass2=request.POST.get('password2')
#        if pass1!=pass2:
#            return HttpResponse("your password and confirm pass are not same.")
    #    my_user=User.objects.create_user(uname,email,pass1)
    #   my_user.save()
    #    return redirect('logi')
    
#    return render(request,'user/signup.html')



        
#staff login
def Login_govt(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    if request.method == "POST":
        username=request.POST.get('uname')
        pass1=request.POST.get('pwd')
        user=authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request,user)
            return redirect('staffdash')
        else:
            return redirect('loggvt')
    return render(request,'loggvt.html')

def Logout_staff(request):
    if not request.user.is_staff:
        return redirect('staffdash')
    logout(request)
    return redirect('staffdash')




def LoginPage(request):   
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = user.username
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("useri")
            else:
                messages.error(request,"Invalid username or password.")
    else:
                messages.error(request,"Invalid username or password.")
                form = AuthenticationForm()
    return render(request=request, template_name="user/logi.html", context={"login_form":form})
   


def Logout_user(request):
    if request.user is not None:
        return redirect('logi')
    logout(request)
    return redirect('logi')





#admin side

def Addservice(request):
    return render(request,'admin/addservice.html')

def Addstaff(request):
    return render(request,'admin/addstaff.html')

def Managestaff(request):
    return render(request,'admin/managestaff.html')

def Manageuser(request):
    #username=request.session['username']
    
    queryset =User.objects.all()
    context ={'Adduser':queryset}  
    return render(request,'admin/manageuser.html',context)

def Viewcomp(request):
    queryset =Regcomplaint.objects.all()
    context ={'regcomplaints':queryset}  
    return render(request,'admin/viewcomp.html',context)

def viewstatuses(request):
    return render(request,'admin/viewstatuses.html')

def Adduseri(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"signup Successfull.")
            return redirect('adduseri')
    messages.error(request,"unsuccessfull registration.invalid information")
    form = NewUserForm()
    return render(request=request, template_name="staff/adduseri.html", context={"register_form":form})

def Viewcomplaints(request):
    return render(request,'staff/viewcomplaints.html')


# def delete_user(request, username):
#     user = User.objects.get(id=username)

#     if request.user.is_admin:
#         confirmation_message = "Are you sure you want to delete this user?"
#     else:
#         confirmation_message = "You do not have permission to delete this user."

#     context = {
#         "user": user,
#         "confirmation_message": confirmation_message,
#     }

# # sourcery skip: merge-nested-ifs
#     if request.method == "POST":
#         if request.POST.get("confirm") == "yes":
#             user.delete()
#             return redirect("/admin/manageuser")

#     return render(request, "admin/manageuser.html", context)
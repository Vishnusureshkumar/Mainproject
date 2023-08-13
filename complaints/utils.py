import time

from django.core.mail import send_mail
from django.conf import settings

def run_this_function():
   print("function started") 
   print("function started")

   time.sleep(2)
   print("function executed")


def send_email_to_client():
   subject = "message from CRS PORTAL"
   message = " Thankyou for submitting your compliants we will solve it shortly"
   from_email =settings.EMAIL_HOST_USER
   recipient_list =["akhilskumarctk@gmail.com"]
   send_mail(subject,message,from_email,recipient_list)


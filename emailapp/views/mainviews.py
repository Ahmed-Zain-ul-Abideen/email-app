from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from emailapp.models import *
import json
from django.http import JsonResponse
from django.template.defaulttags import register
from django.core.paginator import Paginator


# Index View
def index(request):   
    print("Before index def")
    send_invitation_email()
    print("After index def ")
    
    return render(request, 'index.html')

# Email page
def email_page(request):   
    
    
    return render(request, 'invitationmailv3.html')




# Invitation Email Sending View
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_invitation_email():
    print("in email function")
    user_email = 'ashraf.uzair01@gmail.com'
    # user_email = 'az325831@gmail.com'
    
    # Render the HTML email content
    context = {}
    html_content = render_to_string('invitationmailv3.html', context)

    # Create the email
    subject = 'Climate Change Conference!'
    from_email = 'ahmedzain3305@gmail.com'  
    to_email = [user_email]

    email = EmailMultiAlternatives(subject, "", from_email, to_email)
    email.attach_alternative(html_content, "text/html")

     # Send the email
    try:
        email.send()
        print("Email Sent Successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

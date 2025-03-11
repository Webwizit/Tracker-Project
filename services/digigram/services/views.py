from django.shortcuts import redirect, render

def index(request):
    return render(request, 'templates/index.html')

def about(request):
    return render(request, 'templates/about.html')
def Team(request):
    return render(request, 'templates/team.html')

def blog(request):
    return render(request, 'templates/blog.html')

def blog_single(request):
    return render(request, 'templates/blog-single.html')

# views.py

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

def contact(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        subject = f"New message from {full_name}"
        message_body = (
            f"Name: {full_name}\n"
            f"Email: {email}\n\n"
            f"Message:\n{message}"
        )
        
        # Send email using Gmail settings from settings.py
        send_mail(
            subject,
            message_body,
            settings.EMAIL_HOST_USER,   # sender's email
            [settings.EMAIL_HOST_USER], # recipient's email (could be the same as sender)
            fail_silently=False,
        )
        # Optionally, redirect to a thank-you page after sending the email
        return redirect('thank_you')
    
    return render(request, 'contact.html')

def services(request):
    return render(request, 'templates/services.html')

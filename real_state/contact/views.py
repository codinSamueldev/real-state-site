from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

# Create your views here.
def contact_view(request):
    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['message']

        if request.user.is_anonymous:
            from_email = request.POST['email']  # user-provided email
        else:
            from_email = request.user.email  # authenticated user's email

        # Create the email message
        email = EmailMessage(
            subject,
            message,
            from_email,  # Sender email (User's email)
            [settings.EMAIL_HOST_USER],  # Recipient email (Your email)
        )
        
        # Set the 'Reply-To' header
        email.reply_to = [from_email]  # Reply will go to the user's email
        
        # Send the email
        email.send(fail_silently=False)

    return render(request, 'contact/contact.html', {})

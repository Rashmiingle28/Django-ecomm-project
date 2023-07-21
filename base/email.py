from django.conf import settings
from django.core.mail import send_mail


def send_account_activation_email(emali , email_token):
    return 
    subject = 'Your account need to be verified'
    email_from = settings.EMAIL_HOST_USER
    message = 'hi, click on the link to activate your account http://http://127.0.0.1:8000/accounts/activate/{email_token}'
    send_mail(subject , message , email_from , [email])    

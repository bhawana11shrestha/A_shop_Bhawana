from django.conf import settings
from django.core.mail import send_mail

def send_account_activation_email(email,email_token):
    subject = 'Your account needs to be verified'
    email_from = settings.EMAIL_HOST_USER
    message = f'Hi click on the link to activate accounto  '
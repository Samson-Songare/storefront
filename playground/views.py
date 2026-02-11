from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        mail_admins('warning','be careful your site is about to be hacked',html_message='warning')
    except BadHeaderError:
        pass

    return render(request, "hello.html", {'name': 'samson', 'result': ''})

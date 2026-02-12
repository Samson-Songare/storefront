from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name='mails/hello.html',
            context={'name':'Samson'}
            )
        message.send(['sams@gmail.com'])
    except BadHeaderError:
        pass

    return render(request, "hello.html", {'name': 'samson', 'result': ''})

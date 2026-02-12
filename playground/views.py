from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        message = EmailMessage(
            'warning', 'you must be very careful', 'from@samson.com', ['elf@gmail.com'])
        message.attach_file('playground/static/images/halleluya.png')
        message.send()
    except BadHeaderError:
        pass

    return render(request, "hello.html", {'name': 'samson', 'result': ''})

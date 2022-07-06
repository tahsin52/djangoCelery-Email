from django.http import HttpResponse
from django.shortcuts import render

from .tasks import sleepy, send_email_task


def index(request):
    try:
        send_email_task() # 1
        # send_email_task.delay() # 2
    except Exception as e:
        print(e)
    return HttpResponse("<h1>Hello,Task is Done!.</h1>")
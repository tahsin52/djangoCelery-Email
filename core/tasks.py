from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    import time
    time.sleep(duration)
    return None


@shared_task
def send_email_task():
    sleep(10)
    send_mail(
        subject="Celery Task Worked!",
        message="This is a test email from Celery Task!",
        fail_silently=False,
        recipient_list=["reyiy92533@lenfly.com"],
        from_email="reyiy92533@lenfly.com",
    )

    return None
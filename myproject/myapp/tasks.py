from time import sleep
from celery import shared_task


def process_send_email(to_email):
    sleep(10) # Simulate a long-running task
    print(f"Email sent to {to_email}")
    return True

@shared_task
def send_email(to_email):
    # Call to a long-running process
    process_send_email(to_email)
    return "Done!"
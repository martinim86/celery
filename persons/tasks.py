from persons.celery import app
from .send import send_email

@app.task
def send_email():
    send_email()

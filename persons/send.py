# Create your views here.


from django.core.mail import send_mail, EmailMultiAlternatives
RECIPIENTS_EMAIL = ['manager@mysite.com']

def send_email():
    with open('readmewerfsdfs.txt', 'w') as f:
        f.write('Create a new text file!')
    # msg = EmailMultiAlternatives('its send function' '123', '123@gmail.com', RECIPIENTS_EMAIL)
    # msg.send()
    # print('its sand f')

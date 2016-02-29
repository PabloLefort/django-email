from django.core.mail.backends.smtp import EmailBackend
from django.core.mail import EmailMessage
from django.shortcuts import render

def myView(request):
    try:
        backend = EmailBackend(
          host='EMAIL_HOST',
          # Port 587 recomended for SMTP
          port=587,
          username='EMAIL_HOST_USER',
          password='EMAIL_HOST_PASSWORD',
          use_tls=True
        )
        backend.open()
        subject = 'My subject'
        '''
          If you want html message can do:
          from django.template.loader import render_to_string
          message = render_to_string('template.html')
        '''
        message = 'Hi!'
        sender = 'your_email@email.com'
        # List of recipients
        recipients = ['test@email.com']
        email = EmailMessage(subject, message, sender, recipients)
        email.content_subtype = "html"
        backend.send_messages([email])
        backend.close()
    except Exception,e:
        print(e)
        return render(request, "error.html")

    return render(request, "success.html")

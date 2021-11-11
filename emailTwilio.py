import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")


def sendEmail(para, asunto, mensaje):
    message = Mail(
    from_email = 'danielvalenciacordero2@gmail.com',
    to_emails = para,
    subject = asunto,
    html_content = mensaje)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        return "El correo se mando correctamente: "+str(response)
    except Exception as e:
        return str(e)
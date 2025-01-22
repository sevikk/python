from email.message import EmailMessage
import smtplib

email = EmailMessage()
email['from'] = 'Sevikk'
email['to'] = 'sevik.1989@gmail.com'
email['subject'] = 'Hello from Python'
email.set_content("Hello content")

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    smtp_server.send_message(email)
    print('Email was sent')

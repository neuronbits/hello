import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'hungrypy@gmail.com'
password = 'LetsGetItStarted2020'


def send_mail(text='Email Body', subject='Hello World',from_email='Name <hungrypy@gmail.com>',to_emails=None, html=None):
    assert isinstance(to_emails,list) # make sure 'to_emails is list else raise error

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] =', '.join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html is not None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)

    msg_str = msg.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()

    # this below is same as above code
    # with smtplib.SMTP() as server:
    #     server.login()
    #       this one auto quite


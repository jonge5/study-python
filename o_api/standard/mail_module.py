import smtplib
import ssl

port = 587
smtp_server = 'smtp.gmail.com'
sender_email = 'jonge54@gmail.com'
receiver_email = 'jonge5@naver.com'
password = 'zidm izro vmwy sdbu'
message = 'hi'

context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.encode("utf-8"))

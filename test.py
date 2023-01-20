
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# mail_content = '''Hello,
# This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
# Thank You '''
# #The mail addresses and password
# sender_address = 'kaustub.tavaga@gmail.com'
# sender_pass = 'cfzmzeljammgwkie'
# receiver_address = 'pandeykaustubdutt@gmail.com'
# #Setup the MIME
# message = MIMEMultipart()
# message['From'] = sender_address
# message['To'] = receiver_address
# message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
# #The body and the attachments for the mail
# message.attach(MIMEText(mail_content, 'plain'))
# #Create SMTP session for sending the mail
# session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
# session.starttls() #enable security
# session.login(sender_address, sender_pass) #login with mail_id and password
# text = message.as_string()
# session.sendmail(sender_address, receiver_address, text)
# session.quit()
# print('Mail Sent')

import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


# def send_mail(send_from, send_to, subject, text, files=None,
#               server="127.0.0.1"):
#     assert isinstance(send_to, list)

#     msg = MIMEMultipart()
#     msg['From'] = send_from
#     msg['To'] = COMMASPACE.join(send_to)
#     msg['Date'] = formatdate(localtime=True)
#     msg['Subject'] = subject

#     msg.attach(MIMEText(text))

#     for f in files or []:
#         with open(f, "rb") as fil:
#             part = MIMEApplication(
#                 fil.read(),
#                 Name=basename(f)
#             )
#         # After the file is closed
#         part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
#         msg.attach(part)


#     smtp = smtplib.SMTP(server)
#     smtp.sendmail(send_from, send_to, msg.as_string())
#     smtp.close()
    
sender_address = 'kaustub.tavaga@gmail.com'
sender_pass = 'cfzmzeljammgwkie'
receiver_address = 'pandeykaustubdutt@gmail.com'
text = "rdtfccciytvytvutvtvuitvutivt7vtvtvituvitv7tivtvitvgitvigtvtvtvu"
#Setup the MIME
# message = MIMEMultipart()
# message['From'] = sender_address
# message['To'] = receiver_address
# message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
#The body and the attachments for the mail
msg = MIMEMultipart()
msg['From'] = sender_address
msg['To'] = receiver_address #COMMASPACE.join(send_to)
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = 'A test mail sent by Python. It has an attachment.'

msg.attach(MIMEText(text))
files = ["test.pdf"]

for f in files or []:
    with open(f, "rb") as fil:
        part = MIMEApplication(
            fil.read(),
            Name=basename(f)
        )
    # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
    msg.attach(part)
# msg.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = msg.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')

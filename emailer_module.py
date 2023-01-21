import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
def send_email(sender_address,sender_pass,receiver_addresses,subject,body,files):
    try:    
        for receiver_address in receiver_addresses:
            msg = MIMEMultipart()
            msg['From'] = sender_address
            msg['To'] = receiver_address
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = subject
            msg.attach(MIMEText(body))

            for f in files or []:
                with open(f, "rb") as fil:
                    part = MIMEApplication(
                        fil.read(),
                        Name=basename(f)
                    )
                # After the file is closed
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
                msg.attach(part)
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address,sender_pass) #login with mail_id and password
            text = msg.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            print('Mail Sent')

    except Exception as e:
        print(e)
        raise Exception("mail not sent")

# sender_address = 'kaustub.tavaga@gmail.com'
# sender_pass = 'cfzmzeljammgwkie'
# obj = emailer(sender_address,sender_pass)
# receiver_addresses = ['pandeykaustubdutt@gmail.com',"mitali.lohar2002@gmail.com"]
# obj.send(receiver_addresses,"Hello Hello","This is a test mail",["test.pdf"])

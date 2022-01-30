import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "belyjob@gmail.com"
password = 'WBeli60034'
receiver_email =input('Enter reciver email')#input recive email

if(receiver_email.split('@')[1].__contains__('.')!=True):#test validate email
    print('The input is incorrect')
    exit()

subject=input('Enter subject mail')#input subject
if(subject==''):#validate subject
    print('Subject is not null')
    exit()

body= input('Enter body mail')
#create object message
message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = sender_email
message["To"] =receiver_email
#subject+body
part = MIMEText(body, "plain")
message.attach(part)

try:
    context = ssl.create_default_context()
    #send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    print('Success email!!')
except Exception as e:
    print('No send email '+e)
    exit()

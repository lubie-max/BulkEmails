import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

print('hello world')
# this can be read from csv 
emaillist = ['shaikhls2421@gmail.com', 'shaikh.1u64@gmail.com ']
             
def sendMail(fromEmail, toEmail , subject, message):
  msg = MIMEMultipart()
  msg.set_unixfrom('Lubna')
  msg['From']= fromEmail
  msg['To']= toEmail
  msg['subject']= subject
  msg.attach(MIMEText(message))
  mailserver= smtplib.SMTP_SSL('smtpout.secureserver.net',465)
  mailserver.ehlo()
  mailserver.login(os.environ['email'], os.environ['password'])
  
  mailserver.sendEmail(fromEmail, toEmail, msg.as_string)
  mailserver.quit()
  
  
  
  
  
  
for email in emaillist:
  fromMail= 'shaikh.lubna.127.0.0.01@gmail.com'
  toEmail = email
  subject= 'da ta da t a tara '
  message= "let me take you dancing"
  # sendMail(fromMail, toEmail, subject, message)

  print(f'Mail sent to {email}')
  time.sleep(4)

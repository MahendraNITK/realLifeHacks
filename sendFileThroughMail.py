#!/usr/bin/env python
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys

recipients = ['recipient1@domain1.com', 'recipient2@domain2.com'] 
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = str(sys.argv[1])
msg['From'] = 'sender@gmail.com'
msg['Reply-to'] = 'sender@gmail.com'
 
msg.preamble = 'Multipart massage.\n'
 
part = MIMEText("Message Body......")
msg.attach(part)
 
part = MIMEApplication(open(str(sys.argv[2]),"rb").read())
part.add_header('Content-Disposition', 'attachment', filename=str(sys.argv[2]))
msg.attach(part)
 

server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login("sender@gmail.com", "Sender's password")
 
server.sendmail(msg['From'], emaillist , msg.as_string())

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from string import Template

import os
from pathlib import Path
os.chdir(Path(__file__).parent)
#Login credintials
gmail_user = "monikasinghwbs@gmail.com"
gmail_password = "monika9876"

# Create an email container
message = MIMEMultipart()

message["from"] = "Monika"
message["to"] = "monikasinghwbs@gmail.com"
message["subject"] = "Hello Advanced Python"

body = MIMEMultipart("This is my Email Text")

# Alternative : using a templete
#~~~~~~~~~~~~~~~~~~~~~~~
template = Template(Path("template.html").read_text())
body = template.substitute({"name":"Monika"})

# The body of the message
#message.attach(body) --> for simple MIMEText
message.attach(MIMEText(body,"html")) # --> for Html template

#Attach an Image
message.attach(MIMEImage(Path("myimage.PNG").read_bytes()))

#To see the content of my Email container
print(message.as_string())

with smtplib.SMTP(host="smtp.gmail.com",port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(gmail_user,gmail_password)
    smtp.send_message(message)
    print("Sent Successfully !!")
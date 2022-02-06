import smtplib
from typing import Protocol
# Login Credintials
gmail_user = "monikasinghwbs"
gmail_password = "monika9876"

send_from = gmail_user
send_to =["monikasinghwbs@gmail.com","monikarao0101@gmail.com"]
subject = "Test E_mail"
body = "Hello Python"

# achtung:Protocol Text is hard stricred formatted -->Capital\small,spaces etc
email_text = f"""\
From: {send_from}
To: {send_to}
Subject: {subject}
{body}"""

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)

    # Start the connection
    server.ehlo() # Hello Message to server (extended hello), kind of protocal connection command

    # Login to the server
    server.login(gmail_user,gmail_password)

    # Send data
    server.sendmail(send_from,send_to,email_text)

    # Close connection
    server.close()

except:
    print("Something went wrong !!")

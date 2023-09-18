#!/usr/bin/python3

import smtplib
import ssl
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from datetime import date, datetime

# imports from files in this repo
from message import render_message
from wednesday import next_wednesday, is_first_wednesday
from credentials import *


# find the date of the next wednesday. Only proceed, if it will be the
# first wednesday in a month
next_date = next_wednesday()
print(datetime.now())
if not is_first_wednesday(next_date):
    print("Next Wednesday is not the first Wednesday in the month.")
    exit(0)

# format the date properly and render the message texts
next_date_str = next_date.strftime("%d.%m")
text_plain, text_html = render_message(next_date_str)


# assemble a multipart E-Mail. Depending on the settings of the mail client,
# either the html part or the plaintext part will be shown. Thunderbird can
# handle basic markdown in plaintext (bold italic, and so on.)
mail = MIMEMultipart("alternative")
mail["Subject"] = "Diesen Mittwoch: Freifunktreffen auf der c-base"
mail["From"] = mail_from
mail["To"] = mail_to

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text_plain, "plain")
part2 = MIMEText(text_html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
mail.attach(part1)
mail.attach(part2)

# send the mail and show the steps at stdout
s = smtplib.SMTP(smtp_server, port=smtp_port)
print(s.ehlo())
print(s.starttls())
print(s.login(smtp_username, smtp_passwd))

try:
    s.send_message(mail)
    print("sent msg to: " + mail.get("To"))

except:
    print("Verschicken fehlgeschlagen...")

time.sleep(1)

s.close()

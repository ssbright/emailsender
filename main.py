import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #allows access to html file

#for gmail, must turn less secured apps ON

html= Template(Path('index.html').read_text()) #read text reads it as string
email = EmailMessage()
email['from'] = 'rasta dev'
email['to'] = 'mindfulinquisitor@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute(name="TinTin"), 'html') # or {'name': 'TinTin} if there are multiple variables

with smtplib.SMTP(host ='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo() #says hello to server
  smtp.starttls() #connects securely to server
  smtp.login('rastablockchain@gmail.com', 'DevPassword')
  smtp.send_message(email)
print('all good boss!')

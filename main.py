import smtplib
from email.message import EmailMessage

#for gmail, must turn less secured apps ON

email = EmailMessage()
email['from'] = 'rasta dev'
email['to'] = 'mindfulinquisitor@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(' I am a Python Master! Give me money!!!!')

with smtplib.SMTP(host ='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo() #says hello to server
  smtp.starttls() #connects securely to server
  smtp.login('rastablockchain@gmail.com', 'DevPassword')
  smtp.send_message(email)
print('all good boss!')

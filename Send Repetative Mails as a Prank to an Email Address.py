import smtplib  as smtp 

from email.message import EmailMessage

'''
With google expiring user access to less secure apps w.e.f 30/05/2022, most mail address's smtp services won't work so
the user must have a yahoo email account and after activating app password via going to account security section inside
account info of the mail, the user can send emails. In my findings, I could send 10-11 mails at a time, which may not
be the case with you.
'''

#enter your mail address here (I've tried almost everything but only yahoo seems to work)
user = 'ENTER YOUR MAIL ID'

#enter your app password here (don't use your mail's password rather create an app password and enter it here)
password = 'ENTER APP PASSWORD'

#enter user's/sender's email address here 
fr_address = 'ENTER SENDERS MAIL ID'

#enter reciever's email address here
to_address = 'ENTER RECIEVERS MAIL ID'

#enter host address here (use 'smtp.mail.yahoo.com' for yahoo email address i.e. if user has a yahoo email)
smtp_host = 'smtp.mail.yahoo.com' 

#enter host port number here (use 587 for yahoo email address)
smtp_port = 587

#enter subject of the mail here
subject = 'ENTER SUBJECT'

#enter mail content here
msg_text = 'ENTER MAIL CONTENT HERE'

msg_count = 0

#the value of range could be changed upon user's wish, I'm entering 10 here as I could send only 10-11 mails at a time
for b in range(10):

    server = smtp.SMTP(host=smtp_host, port=smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()    
    server.login(user=user, password=password)

    msg = EmailMessage()
    msg['From'] = fr_address
    msg['To'] = to_address
    msg['Subject'] = subject + " " + str(msg_count+1)
    msg.set_payload(msg_text)

    msg_count += 1
        
    server.send_message(msg)
    
    server.close()

print("Code Successfully deployed!")

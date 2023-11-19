import smtplib
sender_email = "yourEmail@gmail.com"
reciever_email =  "recieverEmail@gmail.com"
# password = input(str("Please enter your password"))
SUBJECT = input(str('Please enter the Subject for the mail'))
TEXT = input(str('Please enter the Message for the mail'))
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, 'password')
print("login sucess")
server.sendmail(sender_email, reciever_email, message)
print("horray")
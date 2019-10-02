import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
sender = "haveafreeword@gmail.com"
receiver = str(input("Reciever email: "))

words = open("words.txt","r")
content = open("text.txt","r")

word = words.readlines()
text = content.read()

hmm = input("How many: ")
password = input("Type your password and press enter: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password)
    for countr in range(1, (int(hmm)+1)):
        subject = random.choice(word)
        message = MIMEMultipart("alternative")
        message["Subject"] = subject[:-1]
        message["From"] = sender
        message["To"] = receiver
        message.attach(MIMEText(text, "plain"))
        server.sendmail(sender, receiver, message.as_string())
        print("sent " + str(countr))

words.close()
content.close()

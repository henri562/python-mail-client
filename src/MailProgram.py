import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# construct email message with headers and body
from_addr = "linm@mail.npu.edu"
to_addr = "mengchuanlin@yahoo.com"
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = "CS470 Test Email"

body = ("Hello, I am 12861 from CS470 Section B. Today's "
        "date is: 2/19/2016. My first name is: Mengchuan,"
        " and my last name is: Lin.")
msg.attach(MIMEText(body, 'plain'))

# send message using Google's SMTP server
try:
    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.starttls()
    mail_server.login(from_addr, "hfooa&d06")
    mail_server.sendmail(from_addr, to_addr, msg.as_string())
    print("Email sent")
except smtplib.SMTPException:
    print("Error: unable to send mail")
mail_server.quit()

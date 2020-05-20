import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def sendEmail(email, filePath='/Users/harshshetye/Desktop/graphs'):
    image_data = open(filePath+'/pie.jpg', 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Graph of data collected for COVID 19 Cases in India'
    msg['From'] = 'aditya26sg@gmail.com'
    msg['To'] = email

    text = MIMEText('Pie Chart: National Scale, Bar Chart: Statewise Plot')
    msg.attach(text)

    image1 = MIMEImage(image_data, name=os.path.basename(filePath+'/pie.jpg'))
    msg.attach(image1)

    image_data = open(filePath+'/bar.jpg', 'rb').read()
    image2 = MIMEImage(image_data, name=os.path.basename(filePath+'/bar.jpg'))
    msg.attach(image2)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    s.starttls()

    s.login("aditya26sg@gmail.com", "family11010")
    s.sendmail("aditya26sg@gmail.com", email, msg.as_string())
    s.quit()

    return ("Please check your mail for the Graphs from Aditya Singh and Thank You for using Panther's email service ;)")

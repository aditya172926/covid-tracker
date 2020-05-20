import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def sendEmail(email, filePath='give_the_path_to_the_file_where_you_store_your_2_graphs'):
    image_data = open(filePath+'/pie.jpg', 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Graph of data collected for COVID 19 Cases in India'
    msg['From'] = #enter your emailId
    msg['To'] = email

    text = MIMEText('Pie Chart: National Scale, Bar Chart: Statewise Plot')
    msg.attach(text)

    image1 = MIMEImage(image_data, name=os.path.basename(filePath+'/name_of_the_graph'))
    msg.attach(image1)

    image_data = open(filePath+'/bar.jpg', 'rb').read()
    image2 = MIMEImage(image_data, name=os.path.basename(filePath+'/name_of_the_graph'))
    msg.attach(image2)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    s.starttls()

    s.login("enter_you_email, enter_your_password)  #the email and password must be in " " as in string.
    s.sendmail("enter_your_email", email, msg.as_string())
    s.quit()

    return ("Please check your mail for the Graphs and Thank You for using our email service ;)")

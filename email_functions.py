import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from connection import Connection
from email import parser
from credentials import credentials, email_data


def is_alive():
    conn = Connection()
    
    n_messages = len(conn.connection.list()[1])
    messages = [conn.connection.retr(i+1)[1] for i in range(0, n_messages)]
    messages = ['\n'.join(value.decode('utf8') for value in msg) for msg in messages]
    messages = [str(parser.Parser().parsestr(msg)) for msg in messages]

    conn.close_connection()
    for msg in messages:
        if msg.find('vivo') != -1:
            return True

    return False

def send_email():
    smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtp.starttls()
    smtp.login(credentials['username'], credentials['password'])

    smtp.send_message(get_message())
        
    smtp.quit()

def get_message():
    message = MIMEMultipart()

    message['From'] = credentials['username']
    message['To'] = email_data['person_email']
    message['Subject'] = email_data['subject']
    
    message.attach(MIMEText(email_data['message'], 'plain'))
    return message
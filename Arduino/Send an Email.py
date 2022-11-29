import pyfirmata
import time
import smtplib
import ssl

def send_email():
    port = 465 #For SSL
    smtp_server = 'smtp.gmail.com'
    sender_email = 'alvicviojan@gmail.com'
    receiver_email = 'alvicviojan42@yahoo.com'
    password = 'Akosiwilliam47'
    message = '''Subject: Arduino Notification\n The switch was turned on.'''
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        print("Sending Email...")
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

board = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(board)
it.start()

digital_input = board.get_pin('d:10:i')

while True:
    sw = digital_input.read()
    if sw == True:
        send_email()
        time.sleep(0.1)
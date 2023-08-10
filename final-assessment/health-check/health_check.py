#!/usr/bin/env python3
import psutil
import shutil
import socket
import smtplib
import time
import emails

def sendEmail(subject):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = subject
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

def check_system():
    error_report = []
    # Check CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > 80:
        sendEmail("Error - CPU usage is over 80%")

    # Check disk space
    disk_space = shutil.disk_usage('/')
    if disk_space.percent > 80:
        sendEmail("Error - Available disk space is less than 20%")

    # Check available memory
    available_memory = psutil.virtual_memory().available / (1024 ** 2)  # Convert to MB
    if available_memory < 500:
        sendEmail("Error - Available memory is less than 500MB")

    # Check hostname resolution
    try:
        ip_address = socket.gethostbyname('localhost')
        if ip_address != '127.0.0.1':
            sendEmail("Hostname 'localhost' does not resolve to '127.0.0.1'")
    except socket.error:
        sendEmail("Error - localhost cannot be resolved to 127.0.0.")

if __name__ == "__main__":
    while True:
        check_system()
        time.sleep(60)  # Check every 60 seconds

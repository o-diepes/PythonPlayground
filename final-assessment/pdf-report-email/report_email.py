#!/usr/bin/env python3
import os
import datetime
import reports
import sys
import emails

def get_description_data():
  res_directory = "supplier-data/descriptions"
  fb_files = os.listdir(res_directory)
  print(fb_files)
  result = ""
  for f in fb_files:
    tempResult = ""
    with open(res_directory + "/" + f, 'r') as fp:
        # To store lines
        for i, line in enumerate(fp):
            # read line 4 and 7
            if i == 0:
                tempResult += "name: " + line + "<br/>"
            elif i == 1:
                tempResult += "weight: " + line + "<br/>"
            elif i == 2:
                tempResult += "<br/>"
    result += tempResult
  return result

def main(argv):
  """Process the JSON data and generate a full report out of it."""
  title = "Processed Update on " + datetime.datetime.now().strftime('%B %d, %Y')
  paragraph = get_description_data()
  print("email data:")
  print(paragraph)
  # TODO: turn this into a PDF report
  reports.generate_report("/tmp/processed.pdf", title, paragraph)
  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send_email(message)

if __name__ == "__main__":
  main(sys.argv)

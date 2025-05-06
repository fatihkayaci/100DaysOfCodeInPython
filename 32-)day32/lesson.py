# her pazartesi mail alabileceğim bir uygulama yapacağım

import datetime
import smtplib
from random import choice
email = "fatihkayaci5334@gmail.com"
password = "dzfcgdnhpfzqaimt"

def random_message():
    with open("quotes.txt") as data_file:
        data = data_file.readlines()
        random_data = choice(data)
    return random_data

def mail_send():
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user = email, password = password)
        connection.sendmail(from_addr = email, to_addrs = "fatihkayaci@yahoo.com", msg = f"Subject:Motivation Message \n\n {random_message()}")


now = datetime.datetime.now()

if now.weekday() == 1:
    mail_send()


























# mail send process

# import smtplib

# email = "fatihkayaci5334@gmail.com"
# password = "dzfcgdnhpfzqaimt"

# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user = email, password = password)
#     connection.sendmail(
#         from_addr = email, 
#         to_addrs ="fatihkayaci@yahoo.com", 
#         msg = "Subject:Hello\n\nThis is the body of my email")



# use date labrery

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_weekend = now.weekday()

# date_of_birth = dt.datetime(year = 2000, month = 5, day = 23)
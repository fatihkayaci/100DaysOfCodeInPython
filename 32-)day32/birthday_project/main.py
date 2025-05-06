# https://www.pythonanywhere.com/ python bulutta saklayıp çalıştırmak için

import pandas as pd
import smtplib
from random import choice, randint
import datetime as dt
demo = {}
email = "fatihkayaci5334@gmail.com"
password = "dzfcgdnhpfzqaimt"

def birthday_select():
    global demo
    now = dt.datetime.now()
    with open("birthdays.csv") as data_file:
            data = pd.read_csv(data_file)
            data_list = data.to_dict('records')
            demo = {d["name"]: d for d in data_list if d["month"] == now.month}
            # demo = [d for d in data_list if d["month"] == now.month and d["day"] == now.day]          

def send_mail(to_adress, message):
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user = email, password = password)
        connection.sendmail(from_addr = email, to_addrs = to_adress, msg = message)
        pass

def random_letter_select():
    global demo
    birthday_select()
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    random_letter = choice(letters)
    with open(f"letter_templates/{random_letter}", "r") as data_file:
        data = data_file.read()
        for person in demo.values():
            new_message = data.replace("[NAME]", person["name"])
            send_mail(to_adress = person["email"], message = f"Subject: Birthday Message \n\n{new_message}")

random_letter_select()

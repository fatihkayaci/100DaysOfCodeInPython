import requests
import smtplib
from datetime import datetime
import time

MY_LAT = 41.008240
MY_LONG = 28.978359

email = "fatihkayaci5334@gmail.com"
password = "dzfcgdnhpfzqaimt"

def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user = email, password = password)
        connection.send_message(
            from_addr = email, 
            to_addrs = "fatihkayaci@yahoo.com", 
            msg = "Subject:Look up \n\n The ISS is above you in the sky.")

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
def is_night():
        
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if  sunset < time_now.hour or time_now.hour <= sunrise:
        return True
while True:
    time.sleep(60)
    if is_night and is_iss_overhead:
        send_mail()

# BONUS: run the code every 60 seconds.




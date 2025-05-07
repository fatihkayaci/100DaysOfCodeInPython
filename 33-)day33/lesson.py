import requests
#--------------------- longitude and latitude ------------------------------

# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# data = response.json()

# print(data)

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)

# ---------------------------------------------sunset----------------------------------
MY_LAT = 41.008240
MY_LONG = 28.978359
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters)

data = response.json()
sunsire = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunsire)
print(sunset)



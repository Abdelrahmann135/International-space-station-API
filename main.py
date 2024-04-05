import requests
from datetime import datetime
import smtplib
MY_LNG = 32.657959
MY_LAT = 25.672227
import time

def near_you():
    if space_lat - 5 <= MY_LAT <= space_lat + 5 and space_lng - 5 <= MY_LNG <= space_lng + 5:
        if my_date >= sunset or my_date <= sunrise:
            return True
    else:
        return False


par = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
time_response = requests.get("https://api.sunrise-sunset.org/json", params=par)
time_response.raise_for_status()
data = time_response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

my_date = datetime.now().hour

space_response = requests.get("http://api.open-notify.org/iss-now.json")
space_data = space_response.json()
space_lat = float(space_data["iss_position"]["latitude"])
space_lng = float(space_data["iss_position"]["longitude"])

my_email = "default@gmail.com"
my_pass = "password"
while True:
    time.sleep(60)
    if near_you():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="send_to@gmail.com",
                msg="subject:Look at the sky\n\nThe ISS above you"
                )
    else:
        print("not yet")

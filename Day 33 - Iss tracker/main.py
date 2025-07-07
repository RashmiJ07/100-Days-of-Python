import requests
import datetime as dt
import smtplib

# save your current coordinates
MY_LAT = 19.067881
MY_LNG = 72.844597

MAIL_SMPT = 'smtp.gmail.com'
TO_MAIL = 'jrashmi081@gmail.com'
MY_EMAIL = 'udemylearnpython@gmail.com'
PASSWORD = 'sqac ghhh xmhr qeai'

def is_iss_overhead():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    data = response.json()['iss_position']
    lat = float(data['latitude'])
    lng = float(data['longitude'])
    
    if MY_LAT - 5 <= lat <= MY_LAT+5  or MY_LNG -5 <= lng <= MY_LNG:
        return True

def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted':0
    }
    response = requests.get(' https://api.sunrise-sunset.org/json',params=parameters)
    data = response.json()['results']
    sunrise = int(data['sunrise'].split('T')[1].split(":")[0])
    sunset = int(data['sunset'].split('T')[1].split(":")[0])
    now_time = dt.datetime.now()
    current_hour = now_time.hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True 

if is_night() and is_iss_overhead():
    connection = smtplib.SMTP(MAIL_SMPT)
    connection.starttls()
    connection.login(user=MY_EMAIL,password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=TO_MAIL,
        msg=f"Subject:Look UP 👆\n\n Look up! The ISS is here."
    )
    print(f"Works")

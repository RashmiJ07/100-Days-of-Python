# api endpoints
# api parameters
# api key: api provider can authorised you acces /deny acces
# # track the usage of the api

from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
import os

account_sid = os.environ['ACCT_SID']
auth_token = os.environ['ACCT_TOKEN']
client = Client(account_sid, auth_token)

# print(message.sid)

api_key = '1bd62c6ff4b80a60e2db3e852504ce16'
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast?'

# save your current coordinates
MY_LAT = 27.472834
MY_LNG = 94.911964

parameters = {
    'lat':MY_LAT,
    'lon':MY_LNG,
    'appid':api_key,
    'cnt':4,
}

import requests

response = requests.get(OWM_Endpoint,params=parameters)
response.raise_for_status()
weather_data = response.json()['list'] #[0]['weather']
    
weather_data = [hour['weather'][0]['id'] for hour in weather_data]


if [id < 700 for id in weather_data]:
    print(f"Bring an umbrella")
    message = client.messages\
        .create(
        body="It's going to rain today. Remember to bring an umbrella!"
        ,to='+918879598537' 
        ,from_='+16693057033'   
        )
    print(message.status)
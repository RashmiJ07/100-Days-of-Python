import requests
import datetime as dt

APP_ID = 'a09313e7'
APP_KEY = 'a27b129d4dddd6b014b82e8b0114500b'
AUTH_KEY = 'cmFzaG1pOnExdzJlM3I0dDV5NnU3aThvOXAw'

GENDER = 'female'
WEIGHT_KG = '62.5'
HEIGHT_CM = '165'
AGE = 27

nutri_Enpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

request_headers = {
    'x-app-id':APP_ID,
    'x-app-key':APP_KEY,
}

exercise_inputs = input(f"how many kms: ")
request_params = {
    'query':exercise_inputs,
    'gender':GENDER,
    'weight_kg':WEIGHT_KG,
    'height_cm':HEIGHT_CM,
    'age':AGE,
}

response = requests.post(url=nutri_Enpoint,json=request_params,headers=request_headers)
result = response.json()['exercises'][0]
print(result)


G_Sheet_Enpoint = 'https://api.sheety.co/a38eaf8b305507b5bd56427a96b5cf3e/workoutTracker/workouts'
# response = requests.get(G_Sheet_Enpoint)
# response.raise_for_status()
# print(response.json())

date_ = dt.datetime.now().strftime("%d/%m/%Y")
time_ = dt.datetime.now().strftime("%X")
exercise  = result["name"].title()
duration = result['duration_min']
calories = result['nf_calories']
print(exercise)

sheet_row_params = {'workout':
    {
        'date':date_,
        'time':timestamp(time_),
        'exercise': exercise,
        'duration':duration,
        'calories':calories,
    }
}

aubearer_headers = {
    'Authorization':'Basic cmFzaG1pOnExdzJlM3I0dDV5NnU3aThvOXAw'
}
response = requests.post(url=G_Sheet_Enpoint,json=sheet_row_params,headers=aubearer_headers)
print(response.text)
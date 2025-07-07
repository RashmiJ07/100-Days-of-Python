import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)

#What are the response codes?
## tell us if your request succeded or failed
### 1XX: Hold on something is happening
### 2XX: Here you go, everything is successful, you should get the data
### 3XX: You don't have permission to get this thing so go away
### 4XX: 404 - thing you are looking for doesn't exists
### 5XX: Website is down or there's some other issue with the website

# if response.status_code == 404:
#     raise Exception("Resource doesn't exists")
# elif response.status_code == 401:
#     raise Exception("You are not eligible to access this data")


longitude = response.json()['iss_position']['longitude']
latitude = response.json()['iss_position']['latitude']

iss_position = (longitude,latitude)
print(iss_position)

# ---------- kanye
# from tkinter import *


# def get_quote():
#     pass
#     #Write your code here.



# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="Day 33//Kanye quotes//background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="Day 33//Kanye quotes//kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)



# window.mainloop()
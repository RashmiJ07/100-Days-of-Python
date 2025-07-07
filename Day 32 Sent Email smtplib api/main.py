import datetime as dt
import pandas as pd
import random
import smtplib
##################### Hard Starting Project ######################

# SETUP THE CONNECTION TO SEND THE MAIL
MAIL_SMTP = "smtp.gmail.com"

#credentials 
MY_EMAIL = 'udemylearnpython@gmail.com'
PASSWORD = 'sqac ghhh xmhr qeai'
TO_EMAIL = 'jrashmi081@gmail.com'
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

data = pd.read_csv('Day 32 Sent Email smtplib api//birthdays.csv')
birthdays_dict = {(row.month,row.day):row for index,row in data.iterrows()}
# print(birthdays_dict)

# data_dict = data.to_dict(orient='index')
# birthdays_dict = {(v['month'],v['day']):{'name':v['name'],'email':v['email'],'year':v['year']} for k,v in data_dict.items()}

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
now = dt.datetime.now()
today = (now.month,now.day)

if today in birthdays_dict:
    
    birthday_name = birthdays_dict[today]['name']
    birthay_email = birthdays_dict[today]['email']
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    # HINT: https://www.w3schools.com/python/ref_string_replace.asp
    letter_choice = random.randint(1,3)
    with open(f'Day 32 Sent Email smtplib api\\letter_templates\\letter_{letter_choice}.txt','r') as file:
        birthday_letter = file.read().replace('[NAME]',birthday_name)
        print(birthday_letter)

    # 4. Send the letter generated in step 3 to that person's email address.
    # HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    with smtplib.SMTP(MAIL_SMTP) as connection:
        # For secure connection
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL
            ,to_addrs=birthay_email
            ,msg=f"Subject: Happy Birthday {birthday_name}!!!\n\n{birthday_letter}"
        )

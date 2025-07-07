# import smtplib

# # my_email = 'udemylearnpython@gmail.com'
# my_email = 'udemylearnpython@yahoo.com'
# # password = 'sqac ghhh xmhr qeai'

# # mail_smtp = "smtp.gmail.com"
# mail_smtp = 'smtp.mail.yahoo.com'

# connection = smtplib.SMTP(mail_smtp)

# # Make this connection secure
# connection.starttls()

# # Login
# connection.login(user=my_email, password=password)

# # send the mail
# connection.sendmail(from_addr=my_email
#                     ,to_addrs='udemylearnpython@gmail.com'
#                     ,msg='Subject: Hello\n\nThis is the body of my email')

# connection.close()

import datetime as dt
now = dt.datetime.now()
print(now)
year = now.year
month = now.month
day = now.day
day_of_the_week = now.weekday
date_of_birth = dt.datetime(year=1998, month=1, day=1, hour =0, minute=0, second=0)
print(date_of_birth)



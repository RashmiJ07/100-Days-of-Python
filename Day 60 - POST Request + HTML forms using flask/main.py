from flask import Flask, render_template,request
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
GMAIL_SMTPLIB = "smtp.gmail.com"
class SendMessage:
    def __init__(self):
        self.email= os.environ['OWNER_EMAIL']
        self.password=os.environ['USER_PASSWORD']
    
    def send_message_to_web_owner(self,user_email,name,phone,msg):
        with smtplib.SMTP(GMAIL_SMTPLIB) as connection:
            connection.starttls()
            connection.login(user=user_email,password=self.password)
            connection.sendmail(from_addr=user_email
                                , to_addrs=self.email
                                ,msg=f"Subject:New Message\n\nName:{name}\nEmail:{user_email}\nPhone:{phone}\n{msg}.\n\nThanks!!!")



# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",methods=['POST','GET'])
def contact():
    if request.method=="POST":
        send_email = SendMessage()
        data = request.form
        name = data['name']
        email = data['email']
        phone = data['phone']
        msg = data['message']
        send_email.send_message_to_web_owner(email,name,phone,msg)
        return render_template("contact.html",h1_heading=True)
    return render_template("contact.html",h1_heading=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

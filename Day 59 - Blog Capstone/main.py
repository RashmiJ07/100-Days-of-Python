from flask import Flask,render_template
import requests

app = Flask(__name__)

BLOG_URL = "https://api.npoint.io/c32888ffe8445541623f"
response = requests.get(BLOG_URL)

posts  = response.json()

@app.route("/")
def home():
    return render_template("index.html",all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = None
    for post in posts:
        if post["id"] == post_id:
            requested_post = post
            break

    # Set author link in Python
    if requested_post:
        if requested_post["id"] == 1:
            auth_link = "https://www.ynharari.com/"
        elif requested_post["id"] == 2:
            auth_link = "https://www.khaledhosseini.com/"
        elif requested_post["id"] == 3:
            auth_link = "https://www.chitradivakaruni.com/"
        else:
            auth_link = "#"
    else:
        return "Post not found", 404

    return render_template("post.html", post=requested_post, auth_link=auth_link)
if __name__=="__main__":
    app.run(debug=True)
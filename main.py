from flask import Flask, render_template
import requests
from post import Post

URL = "https://api.npoint.io/52d34040ee9ce8b91db5"
posts = requests.get(url=URL).json()
post_object = []

for post in posts :
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["paragraphe"])
    post_object.append(post_obj)



app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", post_object=post_object)

@app.route("/post/<int:index>")
def next_page(index):
    request_post = None
    for post in post_object :
        if post.id == index :
            request_post=post
    return render_template("next_page.html", request_post=request_post)



if __name__=="__main__":
    app.run(debug=True)
    

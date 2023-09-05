from flask import Flask, render_template
from post import Post
import requests

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()

list_blog = []
for blog_posts in response:
    post = Post(blog_posts["id"], blog_posts["title"], blog_posts["subtitle"], blog_posts["body"])
    list_blog.append(post)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=list_blog)


@app.route("/post/<num>")
def read(num):
    num = int(num)
    return render_template("post.html", num=num, posts=list_blog)


if __name__ == "__main__":
    app.run(debug=True)

 
from flask import Flask, render_template

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("home.html")


# Course Page
@app.route("/course")
def course():
    return render_template("course.html")


# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Run Flask Application
if __name__ == "__main__":
    app.run(debug=True)
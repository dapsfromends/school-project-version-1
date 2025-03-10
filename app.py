from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My First Flask App!</h1>"

@app.route("/about")
def about():
    return "<h2>About Page</h2><p>This is a simple web app built with Flask.</p>"

if __name__ == "__main__":
    app.run(debug=True)
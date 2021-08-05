from flask import Flask, redirect, url_for, render_template

app = Flask(__name__) # creating an instance of flask web application
app.config.from_object()

@app.route("/login") # setting the app route using decorator to slash which is default domain
def login():
    return render_template("login.html")
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/sign-up")
def sign_up():
    return render_template("signup.html")



@app.route("/admin")
def admin():
    pass
    # return redirect(url_for("fun", name="Admin!"))

if __name__ =="__main__":
    app.run(debug=True)
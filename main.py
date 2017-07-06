from flask import Flask, request, render_template, redirect 
import cgi 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup", methods=['POST'])
def add_user():
    #request form responses
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']

    if len(username) < 3 or len(username) > 20:
        error= "Usernames cannot contain spaces and must have between 3-20 characters only"
        return render_template('edit.html', error=error)

    if verify_password != password:
        error2= "Passwords do not match"
        return render_template('edit.html', error2=error2)

    if email != "":
        if len(email) < 3 or len(email) > 20 or "." not in email or "@" not in email:
            error3 = "Please use a valid email"
            return render_template('edit.html', error3=error3)

    else:
        return render_template('welcome.html', username=username)

@app.route("/")
def index():

   return render_template('edit.html')

app.run()
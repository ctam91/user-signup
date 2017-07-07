from flask import Flask, request, render_template, redirect 


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup", methods=['POST'])
def add_user():
    #request form responses
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']

    # creates errors and sets them to an empty string 
    error = ""
    error2 = ""
    error3 = ""

    # check if the username is between 3-20 characters
    if len(username) < 3 or len(username) > 20:
        error= "Usernames cannot contain spaces and must have between 3-20 characters only"

    # check if the password and password confirmation match
    if verify_password != password:
        error2= "Passwords do not match"

    # if the user inputs an email, check that it has between 3-20 characters, contains a period and an "@".
    if email != "":
        if len(email) < 3 or len(email) > 20 or "." not in email or "@" not in email:
            error3 = "Please use a valid email"

    # if there are no errors, return a welcome page
    if not error and not error2 and not error3: 
        return render_template('welcome.html', username=username)

    # returns signup page with error messages if there are errors
    return render_template('edit.html', username=username, password=password, verify_password=verify_password, email=email, error=error, error2=error2, error3=error3) 

@app.route("/")
def index():
    return render_template('edit.html')

app.run()
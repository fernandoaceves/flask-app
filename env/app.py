from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def validate():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       username = request.form.get("fname")
       # getting input with name = lname in HTML form
       password = request.form.get("psw")
       validUser= username[0].isupper()
       validPassword= password.isalnum() and not password.isalpha() and not password.isdigit()
       
       if validUser == True and validPassword == True:
          return "Successful login"
       elif validUser == False:
          return "Invalid user. Must start with capital letter, please "
       elif validPassword == False:
          return "Invalid password. Must contain letters AND numbers"

       #return "User is: " + str(validUser)
    return render_template('index.html')

if __name__=='__main__':
   app.run()
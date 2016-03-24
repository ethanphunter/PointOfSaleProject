from flask import render_template, request, redirect, session, abort, jsonify
from passlib.apps import custom_app_context as pwd_context

loginHtml = """<!DOCTYPE html>
<html>
  <head>
    <title>Log In</title>
  </head>
  <body>
    <h2>Please Log In</h2>
    <form action="/login", method="post">
      username: <br>
      <input type="text" name="username"></input>
      password: <br>
      <input type="password" name="password"></input>
      <input type="submit" name="login">
    </form>
  </body>
</html>"""

logoutHtml = """<!DOCTYPE html>
<html>
  <head>
    <title>Logged Out</title>
  </head>
  <body>
    <h2>Logged Out</h2>
    <a href="/">home</a>
  </body>
</html>"""

def requireLogin():
    if (not session.get("logged_in")):
        return abort(401)

def logout():
    if (not session["logged_in"]):
        return redirect("/")
    else:
        session["current_user"] = None
        print("Logged out")
        session["logged_in"] = False
        return logoutHtml

def login(db):
        if (request.method == "POST"):
            passwordHash = db.getPasswordForUser(request.form["username"])
            print(passwordHash)
            if (passwordHash == []):
                print("No User Found")
                return abort(401)
            else:
                print("Checking password...")
                if (pwd_context.verify(request.form["password"], passwordHash[0][0])):
                    print("password is correct!")
                    session['logged_in'] = True
                    print("logged_in set")
                    session["current_user"] = request.form["username"]
                    print(request.form["username"] + " Logged in")
                    return redirect("/")
                else:
                    print("Wrong password!!")
                    return abort(401)
        else:
            return loginHtml

# from flask import Flask, request, Response, redirect, session, url_for

# app = Flask(__name__)
# app.secret_key = "supersscret"

# @app.route("/", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")

#         if username == "admin" and password == "123":
#             session["user"] = username  # store in session
#             return redirect(url_for("welcome"))
#         else:
#             return Response("Invalid credentials. Try again.", mimetype="text/plain")

#     # Only reached if method is GET
#     return '''
#     <h2>Login Form</h2>
#     <form method="POST">
#         Username: <input type="text" name="username"><br>
#         Password: <input type="password" name="password"><br>
#         <input type="submit" value="Login">
#     </form>
#     '''

# @app.route("/welcome")
# def welcome():
#     if "user" in session:
#         return f'''
#         <h2>Welcome, {session["user"]}</h2>
#         <a href="{url_for('logout')}">Logout</a>
#         '''
#     return redirect(url_for("login"))

# @app.route("/logout")
# def logout():
#     session.pop("user", None)
#     return redirect(url_for("login"))


# # koi bhi error aaye to hame browser mehi dikh jaye
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template

# Créer une instance
app = Flask(__name__)

# Route de decorateur
@app.route('/')
#def index():
#    return "hello"
def index():
    first_name = "ADOU"
    return render_template('index.html', first_name=first_name)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

# Url invalide
@app.errorhandler(404)
def page_not_found(e):
     return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
     return render_template("500.html"), 500


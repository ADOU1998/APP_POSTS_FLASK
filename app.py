from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Créer une instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key"

# Création de la class Form
class NamerForm(FlaskForm):
    name = StringField("Quel est ton  nom ?", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Route de decorateur
@app.route('/')
#def index():
#    return "hello"
def index():
    first_name = "ADOU"
    return render_template("index.html", first_name=first_name)

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

# route de la page name
@app.route('/name', methods = ['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Valider le form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        
        #Méssage d'alerte
        flash('Succès !')
    return render_template("name.html",
        name = name,
        form = form)

# Configuration du serveur
if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
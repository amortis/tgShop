from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'penispenispenis'
Bootstrap(app)


class AddTokenForm(FlaskForm):
    token = StringField(label="Enter your token")
    submit = SubmitField(label="Submit")


@app.route("/")
def home():
    return render_template("index.html", name="Timur", num=5)


@app.route("/settings", methods=["POST", "GET"])
def settings():
    add_token_form = AddTokenForm()
    if add_token_form.validate_on_submit():
        print(add_token_form.token.data)
        return redirect(url_for("home"))
    else:
        return render_template("settings.html", form=add_token_form)


if __name__=="__main__":
    app.run(debug=True)

from flask import Flask, request,render_template, Response

from flask_wtf.csrf import CSRFProtect
from flask import g
from flask import flash
from config import DevelopmentConfig
from models import db
from models import Alumnos
import forms
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.route("/index", methods=["GET","POST"])
def index():
    alumnos_form=forms.UserForm3(request.form)
    
    if request.method == "POST" and alumnos_form.validate():
        alum=Alumnos(nombre=alumnos_form.nombre.data,
                    apaterno=alumnos_form.apaterno.data,
                    email=alumnos_form.email.data)
        #insert into alumnos values()
        db.session.add(alum)
        db.session.commit()
        
    return render_template("index.html", form=alumnos_form)

@app.route("/ABC_Completo", methods=["GET","POST"])
def ABC_Completo():
    alumnos_form=forms.UserForm3(request.form)
    alumnos=Alumnos.query.all()
    return render_template("ABC_Completo.html", alumnos=alumnos) 

@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
    alumnos_form=forms.UsersForm(request.form)
    nom=""
    apaterno=""
    amaterno=""
    edad=""
    correo=""
    if request.method == "POST" and alumnos_form.validate():
        nom=alumnos_form.nombre.data
        apaterno=alumnos_form.apaterno.data
        amaterno=alumnos_form.amaterno.data
        edad=alumnos_form.edad.data
        correo=alumnos_form.correo.data
        mensaje='Bienvenido: {}'.format(nom)
        flash(mensaje)
        print(f"nombre:{nom}")
        print(f"nombre:{apaterno}")
        print(f"nombre:{correo}")
    return render_template("alumnos.html", form=alumnos_form, nom=nom, apa=apaterno, ama=amaterno, edad=edad, correo=correo)

    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
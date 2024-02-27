from wtforms import Form
from wtforms import StringField, TextAreaField,IntegerField, SelectField, RadioField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    nombre=StringField("nombre")
    email=EmailField("correo")
    apaterno=StringField("apaterno")
    materias=SelectField(choices=[('Español','Esp'),('Mat','Matematicas'),('Ingles','Ing')])
    radios= RadioField('Curso',choices=[('1','1'),('2','2'),('3','3')])
    
class UsersForm2(Form):
    nombre=StringField("nombre",
                       [validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingresa nombre valido')])
    
    apaterno=StringField("apaterno")
    
    amaterno=StringField("apaterno")
    
    edad= IntegerField('edad',
                       [validators.number_range(min=1, max=20,message='valor no valido')])
    
    correo=EmailField("correo",
                      [validators.Email(message='Ingresa un correo valido')])
    
class UserForm3(Form):
    id=IntegerField("id")
    nombre=StringField("nombre",[validators.DataRequired(message='el campo es requerido'),
                                 validators.length(min=4, max=10, message='ingresa nombre valido')])
    apaterno=StringField("apaterno")
    email=EmailField("correo",[validators.Email(message='Ingresa un correo valido')])   
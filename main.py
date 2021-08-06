from flask import Flask ,request,make_response,redirect,render_template,session,url_for,flash
#inicializacion de boostrap
from flask_bootstrap import Bootstrap 

from flask_wtf import FlaskForm 
from wtforms.fields import StringField , PasswordField , SubmitField
from wtforms.validators import DataRequired #Para realizar validacion en los datos 

import unittest     #Para la realizacion de la pruebas test

app = Flask(__name__)#creamos una nueva instancia de flask 

#inicializamos  esta instancia de boostrap+
#recordar que el respaldo de boostrap es solo para boostrap 3 de la version del 3.3  hasta 3.7 
bootstrap = Bootstrap(app)

#Ojo en bootstrap ya encontramos un base.html lo que quiere decir que 
#se puede extender de ellos


#Existe una extension llamada flask mensajes para poder enviar correos electronicos ....



todos=['Comprar cafe','Entregar solicitud  ','Pedir una pizza']

#modificamos la configuracion --para la llave secreta en las sesiones  
app.config['SECRET_KEY']='SUPER SECRET'


class LoginForm(FlaskForm):
    username=StringField('Nombre de usuario',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Enviar')



#Esto es para realizar el test

@app.cli.command()
def test():
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)




#manejo del error 400
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)

#@app.errorhandler(500)
#def internal_server_error(error):
#  return render_template('500.html')

#creamos la ruta
@app.route('/')
def index():
    user_ip=request.remote_addr #La propiedad del usuario remote_addr -> brinda la ip del usuario
    response=make_response(redirect('/hello'))
    #response.set_cookie('user_ip',user_ip)#Establecer una cookie que es igual al ip del usuario 

    session['user_ip']= user_ip
    return response #respuesta de flask



#creamos la ruta
@app.route('/hello',methods=['GET','POST'])
def hello():
    user_ip=session.get('user_ip')
    login_form=LoginForm()
    username=session.get('username')


    context={#diccionario contexto
        'user_ip':user_ip,
        'todos':todos,
        'login_form':login_form,
        'username':username
    }

    #Si nos hacen un post y la forma es valida 
    #vamos a guardar el username en la session
    if login_form.validate_on_submit():
        username=login_form.username.data
        session['username']=username#Esto es para guardarlo en la session

        flash('Nombre de usuario registrado con exito')

        return redirect(url_for('index'))


    return render_template('hello.html',**context)
    #**context permite expandir los elementos del diccionario 
    #return 'Hello World Flask Hiro {}'.format(user_ip)

if __name__ == "__main__":
    app.run(port=8080,debug=True)







#Otras variables para usar como session
# request : Informacion sobre la peticion que realiza el browser
# session : Storage que permanece entre cada request
# current_app : La aplicacion actual 
# g : Storage temporal , se reinicia en cada request  







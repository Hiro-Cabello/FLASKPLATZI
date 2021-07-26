from flask import Flask ,request,make_response,redirect,render_template
#inicializacion de boostrap
from flask_bootstrap import Bootstrap 

app = Flask(__name__)#creamos una nueva instancia de flask 

bootstrap = Bootstrap(app)

#Ojo en bootstrap ya encontramos un base.html lo que quiere decir que 
#se puede extender de ellos

todos=['Comprar cafe','Entregar solicitud  ','Pedir una pizza']





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
    response.set_cookie('user_ip',user_ip)#Establecer una cookie que es igual al ip del usuario 
    return response #respuesta de flask



#creamos la ruta
@app.route('/hello')
def hello():
    user_ip=request.cookies.get('user_ip')

    context={#diccionario contexto
        'user_ip':user_ip,
        'todos':todos
    }

    return render_template('hello.html',**context)
    #**context permite expandir los elementos del diccionario 
    #return 'Hello World Flask Hiro {}'.format(user_ip)

if __name__ == "__main__":
    app.run(port=8080,debug=True)







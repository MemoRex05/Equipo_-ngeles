from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import * #LoginManager, login_user, logout_user, login_required,current_user
from models.edits.edit_files import *

#El módulo os en Python proporciona los detalles y la funcionalidad del sistema operativo.
import os 
from os import remove #Modulo  para remover archivo
from os import path #Modulo para obtener la ruta o directorio

from config import config

from models.ModelUser import ModelUser

# Entities
from models.entities.User import User



app=Flask(__name__)

csrf=CSRFProtect()
db = MySQL(app)
login_manager_app=LoginManager(app)
   
def listaAImagenes():
    urlFiles = 'src/static/archivos'
    return (os.listdir(urlFiles))
def listaAImagenes_1():
    urlFiles = 'src/static/archivos_1'
    return (os.listdir(urlFiles))
def listaAImagenes_2():
    urlFiles = 'src/static/archivos_2'
    return (os.listdir(urlFiles))
def listaAImagenes_3():
    urlFiles = 'src/static/archivos_3'
    return (os.listdir(urlFiles))
def listaAImagenes_4():
    urlFiles = 'src/static/archivos_4'
    return (os.listdir(urlFiles))

@login_manager_app.user_loader
def load_user(id):
     return ModelUser.get_by_id(db,id)

@app.route('/')
def index():
    return redirect(url_for('prueba'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':#Una vez ingresando datos entra al metodo POST y los imprime en la consola
        #print(request.form['username'])
        #print(request.form['password'])
        user = User(0,request.form['username'],request.form['password'])
        logged_user=ModelUser.login(db,user)
        if logged_user != None:
             if logged_user.password:
                  login_user(logged_user)
                  if "GUILLERMO" == request.form['username']:
                      return render_template('auth/admin.html', list_Photos = listaArchivos())
                  elif "OSCAR" == request.form['username']:
                        return render_template('auth/adminfem.html',list_Photos = listaArchivos_1())
                  elif "admin_1" == request.form['username']:
                        return render_template('auth/adminfem_2.html',list_Photos = listaArchivos_2())
                  elif "admin_2" == request.form['username']:
                        return render_template('auth/adminvar.html',list_Photos = listaArchivos_3())
                  elif "admin_3" == request.form['username']:
                        return render_template('auth/adminfem_3.html',list_Photos = listaArchivos_4())
             else:
                  flash("Invalid password...")
                  return render_template('auth/login.html')
        else:
            flash("User not found...")
        return render_template('auth/login.html')
    else: #Accede aqui en el else por el metodo GET al principio hasta que envie datos
        return render_template('auth/login.html')

@app.route('/prueba')
def prueba():
     return render_template('auth/prueba.html')

@app.route('/logout')
def logout():
     logout_user()
     return redirect(url_for('login'))
"""
@app.route('/admin')
@login_required
def admin():
     return "<h1>Vista protegida, solo administradores </h1>"

@app.route('/adminfem')
@login_required
def adminfem():
     return "<h1>Vista protegida, solo administradores</h1>"

@app.route('/adminvar')
@login_required
def adminvar():
     return "<h1>Vista protegida, solo administradores</h1>"

@app.route('/adminfem_2')
@login_required
def adminfem_2():
     return "<h1>Vista protegida, solo administradores</h1>"

@app.route('/adminfem_3')
@login_required
def adminfem_3():
     return "<h1>Vista protegida, solo administradores</h1>"
"""

@app.route('/AngelesVar')
def AngelesVar():
     return render_template('auth/galleries/AngelesVar.html', list_Photos = listaAImagenes())

@app.route('/AngelesFem')
def AngelesFem():
     return render_template('auth/galleries/AngelesFem.html', list_Photos = listaAImagenes_1())

@app.route('/AngelesFem_2')
def AngelesFem_2():
     return render_template('auth/galleries/AngelesFem_2.html', list_Photos = listaAImagenes_2())

@app.route('/AngelesVar_2')
def AngelesVar_2():
     return render_template('auth/galleries/AngelesVar_2.html', list_Photos = listaAImagenes_3())

@app.route('/AngelesFem_3')
def AngelesFem_3():
     return render_template('auth/galleries/AngelesFem_3.html', list_Photos = listaAImagenes_4())

@app.route('/guardar-foto', methods=['GET', 'POST'])
@login_required
def RegistrarFoto():
      
      
    if current_user.fullname == 'Guillermo Angeles':
       Enlace = 'static/archivos'
    if current_user.fullname == 'Oscar Angeles':
       Enlace = 'static/archivos_1'
    if current_user.fullname == 'administrador_1':
       Enlace = 'static/archivos_2'
    if current_user.fullname == 'administrador_2':
       Enlace = 'static/archivos_3'
    if request.method == 'POST':
        if(request.files['archivo']):
           #Script para archivo
           file     = request.files['archivo']
           basepath = path.dirname (__file__) #La ruta donde se encuentra el archivo actual
           filename = secure_filename(file.filename) #Nombre original del archivo
                
           #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
           extension           = path.splitext(filename)[1]
           nuevoNombreFile     = stringAleatorio() + extension
        
           upload_path = path.join (basepath, Enlace, nuevoNombreFile) 
           file.save(upload_path)
    if current_user.fullname == 'Guillermo Angeles':
        return render_template('auth/admin.html', list_Photos = listaArchivos())
    if current_user.fullname == 'Oscar Angeles':
        return render_template('auth/adminfem.html', list_Photos = listaArchivos_1())
    if current_user.fullname == 'administrador_1':
        return render_template('auth/adminfem_2.html', list_Photos = listaArchivos_2())
    if current_user.fullname == 'administrador_2':
        return render_template('auth/adminvar.html', list_Photos = listaArchivos_3())

@app.route('/<string:nombreFoto>', methods=['GET','POST'])
@login_required
def EliminarFoto(nombreFoto=''):
    
    if current_user.fullname == 'Guillermo Angeles':
       Enlace = 'static/archivos'
    if current_user.fullname == 'Oscar Angeles':
       Enlace = 'static/archivos_1'
    if current_user.fullname == 'administrador_1':
       Enlace = 'static/archivos_2'
    if current_user.fullname == 'administrador_2':
       Enlace = 'static/archivos_3'
    if request.method == 'GET': 
         #print(nombreFoto) #Nombre del archivo subido
         basepath = path.dirname (__file__) #C:\xampp\htdocs\elmininar-archivos-con-Python-y-Flask\app
         url_File = path.join (basepath, Enlace, nombreFoto)
         #print(url_File)
        
         #verifcando si existe el archivo, con la funcion (path.exists) antes de de llamar remove 
         # para eliminarlo, con el fin de evitar un error si no existe.admin
         if path.exists(url_File):
            remove(url_File) #Borrar foto desde la carpeta
            #os.unlink(url_File) #Otra forma de borrar archivos en una carpeta
    if current_user.fullname == 'Guillermo Angeles':
        return render_template('auth/admin.html', list_Photos = listaAImagenes())
    if current_user.fullname == 'Oscar Angeles':
        return render_template('auth/adminfem.html', list_Photos = listaAImagenes_1())
    if current_user.fullname == 'administrador_1':
        return render_template('auth/adminfem_2.html', list_Photos = listaAImagenes_2())
    if current_user.fullname == 'administrador_2':
        return render_template('auth/adminvar.html', list_Photos = listaAImagenes_3())
        

#---------------------CRUD de usuarios----------------------------------

def status_401(error):
     return redirect(url_for('login'))

def status_404(error):
     return "<h1>Página no encontrada</h1>",404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
from random import sample
from flask_login import  login_required
#Para subir archivo tipo foto al servidor
from werkzeug.utils import secure_filename 

import os

def stringAleatorio():
    #Generando string aleatorio
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio
  
  
#Funcion que recorre todos los archivos almacenados en la carpeta (archivos) 
@login_required #Funcion que pide autentificacion para acceder a esta ruta
def listaArchivos():
    urlFiles = 'src/static/archivos'
    return (os.listdir(urlFiles))

@login_required #Funcion que pide autentificacion para acceder a esta ruta
def listaArchivos_1():
    urlFiles = 'src/static/archivos_1'
    return (os.listdir(urlFiles))

@login_required #Funcion que pide autentificacion para acceder a esta ruta
def listaArchivos_2():
    urlFiles = 'src/static/archivos_2'
    return (os.listdir(urlFiles))

@login_required #Funcion que pide autentificacion para acceder a esta ruta
def listaArchivos_3():
    urlFiles = 'src/static/archivos_3'
    return (os.listdir(urlFiles))

@login_required #Funcion que pide autentificacion para acceder a esta ruta
def listaArchivos_4():
    urlFiles = 'src/static/archivos_4'
    return (os.listdir(urlFiles))

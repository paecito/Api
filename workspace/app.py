from flask import Flask, jsonify, render_template, request
from flask_restful import Resource, Api
import blogger
import mainKodi
import xbmc
import json
import os
import cgi





app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

#@app.route("/enviar", methods=['POST'])
#def enviar():
    #id_blog = '62.117.142.13:8085'
    #nombre = 'sdkodiblog@gmail.com'
    #contrasena = 'blogkodisd'
    #servidor = '185572784043208024'
    
    #id_blog = request.form['id_blog']
    #nombre = request.form['usuario']
    #contrasena = request.form['contrasena']
    #servidor = request.form['servidor']
    #mainKodi.autentificar(nombre,contrasena,servidor,id_blog)
    #mainKodi.ult_pel()
    #pelicula = json.loads(open('pelis.json').read())
    #return jsonify({'pelicula' : pelicula})
    #render_template('final.html')
    #mainKodi.ult_pel()

    

@app.route("/postear", methods=['POST'])
def posting():
    mainKodi.ult_pel()
    #pelicula = json.loads(open('pelis.json').read())
    pelicula = xbmc.load_json('pelis.json')
    
    #pelicula = xbmc.load_json(pelis.json)
    mainKodi.post_ultima_peli()
    return jsonify({'pelicula' : pelicula})
    #return render_template('final.html')
    
    
#@app.route("/index")
#def index():
#    return render_template('postear.html')
    
if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8081)))
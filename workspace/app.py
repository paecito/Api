from flask import Flask, jsonify
from flask_restful import Resource, Api
import blogger
import mainKodi
import xbmc
import json
import os
import render_template




app = Flask(__name__)


@app.route("/index", methods=['GET'])
def index():
    return render_template('postear.html')
    

@app.route("/postear", methods=['GET'])
def posting():
    mainKodi.ult_pel()
    #pelicula = json.loads(open('pelis.json').read())
    pelicula = json.loads(open('pelis.json').read())
    
    #pelicula = xbmc.load_json(pelis.json)
    mainKodi.post_ultima_peli()
    return jsonify({'pelicula' : pelicula})
    #return render_template('final.html')
    
    
#@app.route("/index")
#def index():
#    return render_template('postear.html')
    
if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8081)))
"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Personajes, Planetas, Favoritos
import datetime
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    query = User.query.all()
    results = list(map(lambda x: x.serialize(), query))

    return jsonify(results), 200

@app.route('/user/<int:id>', methods=['GET'])
def macheo_informacion_user(id):

    usuario = User.query.get(id)
    if usuario is None:
        raise APIException('Usuario not found', status_code=404)
    results = usuario.serialize()
    

    return jsonify(results), 200

@app.route('/personajes', methods=['GET'])
def personajes_todos():

    query = Personajes.query.all()
    results = list(map(lambda x: x.serialize2(), query))

    return jsonify(results), 200

@app.route('/personajes/<int:id>', methods=['GET'])
def personaje_unico(id):

    personaje = Personajes.query.get(id)
    if personaje is None:
        raise APIException('Personaje not found', status_code=404)
    results = personaje.serialize2()

    return jsonify(results), 200

@app.route('/personajes', methods=['POST'])
def add_personaje():

    # recibir info del request
    request_body = request.get_json()
    print(request_body)

    per = Personajes(name=request_body["name"], heigth=request_body["heigth"], mass=request_body["mass"], hair_color=request_body["hair_color"], skin_color=request_body["skin_color"], eye_color=request_body["eye_color"], birth_year=request_body["birth_year"],  gender=request_body["gender"], homeworld=request_body["homeworld"], films=request_body["films"])
    db.session.add(per)
    db.session.commit()

    return jsonify("Un exito, se ha agregado el personaje"), 200


@app.route('/planetas', methods=['GET'])
def planetas_todos():

    query = Planetas.query.all()
    results = list(map(lambda x: x.serialize2(), query))

    return jsonify(results), 200

@app.route('/planetas/<int:id>', methods=['GET'])
def planeta_unico(id):

    planeta = Planetas.query.get(id)
    if planeta is None:
        raise APIException('Planeta not found', status_code=404)
    results = planeta.serialize2()

    return jsonify(results), 200

@app.route('/planetas', methods=['POST'])
def add_fav_planeta():

    # recibir info del request
    request_body = request.get_json()
    print(request_body)

    per = Planetas(name=request_body["name"], climate=request_body["climate"], orbital_period=request_body["orbital_period"], rotation=request_body["rotation"], terrain=request_body["terrain"])
    db.session.add(per)
    db.session.commit()

    return jsonify("Un exito, se ha agregado el planeta"), 200


@app.route('/favoritos', methods=['GET'])
def favoritos_todos():

    query = Favoritos.query.all()
    results = list(map(lambda x: x.serialize2(), query))

    return jsonify(results), 200

@app.route('/favoritos/<int:id>', methods=['GET'])
def favoritos_unico(id):

    favoritos = Favoritos.query.get(id)
    if favoritos is None:
        raise APIException('Favorito not found', status_code=404)
    results = favoritos.serialize2()

    return jsonify(results), 200

@app.route('/favoritos', methods=['POST'])
def add_fav_favoritos():

    # recibir info del request
    request_body = request.get_json()
    print(request_body)

    pera = Favoritos(usuario_id=request_body["usuario_id"], planeta_id=request_body["planeta_id"], personaje_id=request_body["personaje_id"])
    db.session.add(pera)
    db.session.commit()

    return jsonify("Un exito, se ha agregado el favorito"), 200


@app.route('/del_favoritos/<int:id>', methods=['DELETE'])
def del_fav(id):

    # recibir info del request
    
    fav = Favoritos.query.get(id)
    if fav is None:
        raise APIException('Favorite not found', status_code=404)

    db.session.delete(fav)

    db.session.commit()

    return jsonify("Borraste bien la informacion"), 200



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

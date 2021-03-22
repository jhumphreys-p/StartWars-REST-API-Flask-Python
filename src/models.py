from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    genero = db.Column(db.String(250), nullable=False)
    

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "genero": self.genero
            # do not serialize the password, its a security breach
        }

class Personajes(db.Model):
    __tablename__ = 'personajes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    heigth = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    homeworld = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Personajes %r>' % self.name

    def serialize2(self):
        return {
            "id": self.id,
            "name": self.name,
            "heigth": self.heigth,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld,
            "films": self.films
        }

class Planetas(db.Model):
    __tablename__ = 'planetas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.String(250), nullable=False)
    rotation = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planetas %r>' % self.name

    def serialize2(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "orbital_period": self.orbital_period,
            "rotation": self.rotation,
            "terrain": self.terrain
        }

class Favoritos(db.Model):
    __tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planeta_id = db.Column(db.Integer, db.ForeignKey('planetas.id'))
    personaje_id = db.Column(db.Integer, db.ForeignKey('personajes.id'))
    personaje = db.relationship("Personajes")
    planeta = db.relationship("Planetas")
    usuario = db.relationship("User")

    def __repr__(self):
        return '<Favoritos %r>' % self.name


    def serialize2(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planeta_id": self.planeta_id,
            "personaje_id": self.planeta_id,
            #"personaje": self.personaje,
            #"planeta": self.planeta,
            #"usuario": self.usuario
        }   
from flask import Flask, app, render_template, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ejercicio2db = Flask(__name__)
ejercicio2db.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#ejercicio2db.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Chaohola@localhost/ejercicio2db'
ejercicio2db.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Chaohola@localhost:5432/ejercicio2db'

'''mydb = mysql.connector.connect(
  host="localhost",
  user="smeza",
  password="Chaohola",
  database="ejercicio2db"
)'''


db = SQLAlchemy(ejercicio2db)
ma = Marshmallow(ejercicio2db)

class Profesor(db.Model):
    _tablename_ = 'Profesor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    colegio = db.Column(db.String(80), nullable=False)
    distrito = db.Column(db.String(80), nullable=False)
    profesion = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f'<Profesor: {self.id}, {self.nombre}, {self.apellido}, {self.colegio}, {self.distrito}, {self.profesion}>'

class ProfesorSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'apellido', 'colegio', 'distrito', 'profesion')

class Alumno(db.Model):
    _tablename_ = 'alumno'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    colegio = db.Column(db.String(80), nullable=False)
    distrito = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f'<Profesor: {self.id}, {self.nombre}, {self.apellido}, {self.colegio}, {self.distrito}>'

class AlumnoSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'apellido', 'colegio', 'distrito')

class Curso(db.Model):
    _tablename_ = 'curso'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    tipo = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f'<Profesor: {self.id}, {self.nombre}, {self.tipo}>'

class Seccion(db.Model):
    _tablename_ = 'seccion'
    id = db.Column(db.Integer, primary_key=True)
    salon = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f'<Profesor: {self.id}, {self.salon}>'

db.create_all()
profesor_schemas = ProfesorSchema(many=True)
alumno_schemas = AlumnoSchema(many=True)

@ejercicio2db.route('/')
def index():
    #a = "Profesor <div>" + "Nombre <div>" + ",".join([p.nombre for p in Profesor.query.all()]) + "<div> Apellido <div>" + ",".join([p.apellido for p in Profesor.query.all()]) + "<div> Colegio <div>" + ",".join([p.colegio for p in Profesor.query.all()]) + "<div> Distrito <div>"+ ",".join([p.distrito for p in Profesor.query.all()]) + "<div> Profesion <div>"+ ",".join([p.profesion for p in Profesor.query.all()]) + "<div> Profesor <div>" + "Nombre <div>" + ",".join([p.nombre for p in Alumno.query.all()]) + "<div> Apellido <div>" + ",".join([p.apellido for p in Alumno.query.all()]) + "<div> Colegio <div>" + ",".join([p.colegio for p in Alumno.query.all()]) + "<div> Distrito <div>"+ ",".join([p.distrito for p in Alumno.query.all()]) + "<div> Curso <div>" + "Nombre <div>" + ",".join([p.nombre for p in Curso.query.all()]) + "<div> Tipo <div>" + ",".join([p.tipo for p in Curso.query.all()]) + "<div> Seccion <div>" + ",".join([p.salon for p in Seccion.query.all()])
    profesores = Profesor.query.all()
    alumnos = Alumno.query.all()
    resultado = profesor_schemas.dump(profesores)
    resultado1 = profesor_schemas.dump(alumnos)
    #return profesor_schemas.jsonify(resultado)
    return render_template('index2.html', data = resultado, dataAlumno = resultado1 )

if __name__ == '__main__':
    ejercicio2db.run(host="0.0.0.0", port=5001, debug=True)
else:
    print('using global variables from flask')
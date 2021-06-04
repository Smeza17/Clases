from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

rappi = Flask(__name__)
rappi.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
rappi.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Chaohola@localhost:5432/ejercicio3db'
db = SQLAlchemy(rappi)

class Cliente(db.Model):
    __tablename_ = 'Cliente'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable = False)
    destino = db.Column(db.String(150), nullable = False)
    
db.create_all()

@rappi.route('/create', methods=['POST'])
def create_todo_post():
    print("inserting using post method")
    nombre = request.form.get("nombre")
    destino = request.form.get("destino")
    todo = Cliente(destino=destino)
    todo1 = Cliente(nombre=nombre)
    db.session.add([todo, todo1])
    db.session.commit()
    #return 'succes'
    return redirect(url_for('index'))

@rappi.route('/')
def index():
    return render_template('index.html', data = Cliente.query.all())

if __name__ == '__main__':
    rappi.run(host="0.0.0.0", port=5000, debug=True)
else:
    print('using global variables from flask')
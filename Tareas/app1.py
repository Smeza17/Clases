from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import user

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine('postgresql://postgres:Chaohola@localhost:5432/ejercicio2db')
Base = declarative_base()

class Profe(Base):
    __tablename__ = 'profesor'
    
    id = Column(Integer(), primary_key=True)
    nombre = Column(String(80), nullable=False)
    apellido = Column(String(80), nullable=False)
    edad = Column(Integer(), nullable=False)
    distrito = Column(String(80), nullable=False)

    def __repr__(self):
        return f'<Profe: {self.id}, {self.nombre}, {self.apellido}, {self.edad}, {self.distrito}>'

Session = sessionmaker(engine)
session = Session()

@app.route('/')
def index():
    users = session.query(Profe).all()
    for user in users:
        print(user)
        return str(user.created_at)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    n1 = Profe(nombre='Armando', apellido='Perez', edad='30',distrito='Surco')
    n2 = Profe(nombre='Aron', apellido='Rojas', edad='31',distrito='Surco')
    n3 = Profe(nombre='Juan', apellido='Neyra', edad='32',distrito='Miraflores')
    n4 = Profe(nombre='Pedro', apellido='Meza', edad='33',distrito='Surco')
    n5 = Profe(nombre='Leon', apellido='Vedia', edad='34',distrito='Chorrillos')
    n6 = Profe(nombre='Adolfo', apellido='Pulido', edad='35',distrito='Surco')
    n7 = Profe(nombre='Pablo', apellido='Costa', edad='36',distrito='Comas')
    n8 = Profe(nombre='Gabriel', apellido='Baur', edad='37',distrito='Ate')
    n9 = Profe(nombre='Kevin', apellido='Cortijo', edad='38',distrito='Miraflores')
    n10 = Profe(nombre='Mauricio', apellido='Dien', edad='39',distrito='Callao')

    session.add(n1)
    session.add(n2)
    session.add(n3)
    session.add(n4)
    session.add(n5)
    session.add(n6)
    session.add(n7)
    session.add(n8)
    session.add(n9)
    session.add(n10)

    session.commit()
    

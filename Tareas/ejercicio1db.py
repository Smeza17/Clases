import psycopg2
import mysql.connector
#connection = psycopg2.connect('dbname=ejercicio1db user=postgres password=Chaohola')
#connection = psycopg2.connect('dbname=ejercicio1db user=root password=Chaohola host=localhost' )

mydb = mysql.connector.connect(
  host="localhost",
  user="smeza",
  password="Chaohola",
  database="ejercicio1db"
)

#cursor = connection.cursor()
cursor = mydb.cursor()
cursor.execute('drop table if exists profesor;')
cursor.execute('drop table if exists alumno;')
cursor.execute('drop table if exists curso;')
cursor.execute('drop table if exists seccion;')

cursor.execute('''
    create table profesor(
        id INTEGER PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL,
        colegio VARCHAR(50) NOT NULL,
        distrito VARCHAR(50) NOT NULL,
        profesion VARCHAR(50) NOT NULL
    );''')

cursor.execute('''
    create table alumno(
        id INTEGER PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL,
        colegio VARCHAR(50) NOT NULL,
        distrito VARCHAR(50) NOT NULL
    );''')

cursor.execute('''
    create table curso(
        id INTEGER PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        tipo VARCHAR(50) NOT NULL
    );''')

cursor.execute('''
    create table seccion(
        id INTEGER PRIMARY KEY,
        salon VARCHAR(50) NOT NULL
    );''')

cursor.execute('insert into profesor(id, nombre, apellido, colegio, distrito, profesion) values(%s, %s, %s, %s, %s, %s);', (1, 'Armando', 'Perez', 'Carmelita', 'Surco', 'Ingeniero'))
cursor.execute('insert into profesor(id, nombre, apellido, colegio, distrito, profesion) values(%s, %s, %s, %s, %s, %s);', (2, 'Aron', 'Rojas', 'Inmaculada', 'Surco', 'Economista'))
cursor.execute('insert into profesor(id, nombre, apellido, colegio, distrito, profesion) values(%s, %s, %s, %s, %s, %s);', (3, 'Juan', 'Neyra', 'Champana', 'Miraflores', 'Psicologo'))
cursor.execute('insert into profesor(id, nombre, apellido, colegio, distrito, profesion) values(%s, %s, %s, %s, %s, %s);', (4, 'Pedro', 'Neyra', 'Champana', 'Miraflores', 'Psicologo'))
cursor.execute('insert into profesor(id, nombre, apellido, colegio, distrito, profesion) values(%s, %s, %s, %s, %s, %s);', (5, 'Leon', 'Vedia', 'Inmaculada', 'Chorrilos', 'Biologo'))
cursor.execute('insert into profesor(id, nombre, apellido, colegio, distrito, profesion) values(%s, %s, %s, %s, %s, %s);', (6, 'Adolfo', 'Pulido', 'Inmaculada', 'Surco', 'Matematico'))
cursor.execute('insert into profesor(id, nombre, apellido, colegio, distrito, profesion) values(%s, %s, %s, %s, %s, %s);', (7, 'Pablo', 'Costa', 'Carmelita', 'Comas', 'Biologo'))
cursor.execute('insert into profesor(id, nombre, apellido, colegio, distrito, profesion) values(%s, %s, %s, %s, %s, %s);', (8, 'Gabriel', 'Baur', 'Champana', 'Ate', 'Matematico'))
cursor.execute('insert into profesor(id, nombre, apellido, colegio, distrito, profesion) values(%s, %s, %s, %s, %s, %s);', (9, 'Kevin', 'Cortijo', 'Carmelita', 'Miraflores', 'Antropologo'))
cursor.execute('insert into profesor(id, nombre, apellido, colegio, distrito, profesion) values(%s, %s, %s, %s, %s, %s);', (10, 'Mauricio', 'Dien', 'Champana', 'Callao', 'Sociologo'))

cursor.execute('insert into alumno(id, nombre, apellido, colegio, distrito) values(%s, %s, %s, %s, %s);', (1, 'Sebastian', 'Meza', 'Inmaculada', 'Surco'))
cursor.execute('insert into alumno(id, nombre, apellido, colegio, distrito) values(%s, %s, %s, %s, %s);', (2, 'Francisco', 'Tomo', 'Champana', 'Chorrilos'))
cursor.execute('insert into alumno(id, nombre, apellido, colegio, distrito) values(%s, %s, %s, %s, %s);', (3, 'Jorge', 'Mendoza', 'Carmelita', 'Comas'))
cursor.execute('insert into alumno(id, nombre, apellido, colegio, distrito) values(%s, %s, %s, %s, %s);', (4, 'George', 'Alva', 'Inmaculada', 'Miraflores'))
cursor.execute('insert into alumno(id, nombre, apellido, colegio, distrito) values(%s, %s, %s, %s, %s);', (5, 'Miguel', 'Prado', 'Champana', 'Chorrillos'))
cursor.execute('insert into alumno(id, nombre, apellido, colegio, distrito) values(%s, %s, %s, %s, %s);', (6, 'Carlos', 'Garcia', 'Inmaculada', 'Surco'))
cursor.execute('insert into alumno(id, nombre, apellido, colegio, distrito) values(%s, %s, %s, %s, %s);', (7, 'Daniel', 'Rojas', 'Champana', 'Surco'))
cursor.execute('insert into alumno(id, nombre, apellido, colegio, distrito) values(%s, %s, %s, %s, %s);', (8, 'Bryan', 'Landa', 'Carmelita', 'Chorrillos'))
cursor.execute('insert into alumno(id, nombre, apellido, colegio, distrito) values(%s, %s, %s, %s, %s);', (9, 'Vidic', 'Mori', 'Carmelita', 'Ate'))
cursor.execute('insert into alumno(id, nombre, apellido, colegio, distrito) values(%s, %s, %s, %s, %s);', (10, 'Sixto', 'Diaz', 'Inmaculada', 'Comas'))

cursor.execute('insert into curso(id, nombre, tipo) values(%s, %s, %s);', (1, 'Matematica','sincrona'))
cursor.execute('insert into curso(id, nombre, tipo) values(%s, %s, %s);', (2, 'Comunicacion', 'sincrona'))
cursor.execute('insert into curso(id, nombre, tipo) values(%s, %s, %s);', (3, 'Quimica', 'asincrona'))
cursor.execute('insert into curso(id, nombre, tipo) values(%s, %s, %s);', (4, 'Historia', 'asincrona'))
cursor.execute('insert into curso(id, nombre, tipo) values(%s, %s, %s);', (5, 'Civica', 'sincrona'))
cursor.execute('insert into curso(id, nombre, tipo) values(%s, %s, %s);', (6, 'Ingles', 'asincrona'))
cursor.execute('insert into curso(id, nombre, tipo) values(%s, %s, %s);', (7, 'Arte', 'sincrona'))
cursor.execute('insert into curso(id, nombre, tipo) values(%s, %s, %s);', (8, 'Musica', 'sincrona'))
cursor.execute('insert into curso(id, nombre, tipo) values(%s, %s, %s);', (9, 'Biologia', 'asincrona'))
cursor.execute('insert into curso(id, nombre, tipo) values(%s, %s, %s);', (10,'Informatica', 'asincrona'))

cursor.execute('insert into seccion(id, salon) values(%s, %s);', (1,'a'))
cursor.execute('insert into seccion(id, salon) values(%s, %s);', (2,'a'))
cursor.execute('insert into seccion(id, salon) values(%s, %s);', (3,'b'))
cursor.execute('insert into seccion(id, salon) values(%s, %s);', (4,'b'))
cursor.execute('insert into seccion(id, salon) values(%s, %s);', (5,'b'))
cursor.execute('insert into seccion(id, salon) values(%s, %s);', (6,'c'))
cursor.execute('insert into seccion(id, salon) values(%s, %s);', (7,'d'))
cursor.execute('insert into seccion(id, salon) values(%s, %s);', (8,'a'))
cursor.execute('insert into seccion(id, salon) values(%s, %s);', (9,'c'))
cursor.execute('insert into seccion(id, salon) values(%s, %s);', (10,'d'))

cursor.execute('select * from profesor;')
result1 = cursor.fetchall()
print('result1: ', result1)

cursor.execute('select * from alumno;')
result2 = cursor.fetchall()
print('result2: ', result2)

cursor.execute('select * from curso;')
result3 = cursor.fetchall()
print('result3: ', result3)

cursor.execute('select * from seccion;')
result4 = cursor.fetchall()
print('result4: ', result4)

mydb.commit()
mydb.close()
#connection.commit()
#connection.close()
cursor.close()

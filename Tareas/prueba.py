import psycopg2



def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE profesor (
            id INTEGER PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL
        )
        """,
        """ CREATE TABLE estudiante (
                id INTEGER PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL
                )
        """,
        """
        CREATE TABLE curso (
            nombre VARCHAR(100) NOT NULL
        )
        """,
        """
        CREATE seccion (
            id INTEGER PRIMARY KEY
        )
        """)
    conn = None
    try:
        # read the connection parameters
        
        # connect to the PostgreSQL server
        conn = psycopg2.connect('dbname=ejercicio1db user=postgres password=Chaohola')
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
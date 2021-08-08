import psycopg2                                                                

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect("dbname=docker host=postgres user=postgres password=example")
        
        # crear cursor 1
        cur = conn.cursor()
        
	# Información DB
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
	        

        # Consulta #1
        cur.execute("SELECT * FROM cropstats WHERE area = 'Argentina' AND year=2019 AND magnitud='Yield' AND item='Soybeans'")

        row = cur.fetchone()

        while row is not None:
            print('El rendimiento por ha promedio en Argentina en 2019 para Soja es de ',row[9])
            row = cur.fetchone()

        # Consulta #2
        cur.execute("SELECT * FROM cropstats WHERE area = 'Brazil' AND year=2019 AND magnitud='Yield' AND item='Soybeans'")

        row = cur.fetchone()

        while row is not None:
            print('El rendimiento por ha promedio en Brasil en 2019 para Soja es de ',row[9])
            row = cur.fetchone()

        # Consulta #3
        cur.execute("SELECT * FROM cropstats WHERE area = 'Argentina' AND year=2019 AND magnitud='Production' AND item='Soybeans'")

        row = cur.fetchone()

        while row is not None:
            print('El total producido en Argentina en 2019 para Soja es de ',row[9], 'toneladas')
            row = cur.fetchone()

        # Consulta #4
        cur.execute("SELECT * FROM cropstats WHERE area = 'Brazil' AND year=2019 AND magnitud='Production' AND item='Soybeans'")

        row = cur.fetchone()

        while row is not None:
            print('El total producido en 2019 Brasil para Soja es de ',row[9],'toneladas')
            row = cur.fetchone()




       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()

import os
import psycopg2

DATABASE_URL = os.environ['DB_URI']
DB_CREATED = os.environ['DB_CREATED']


def pg_get_db():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    return conn


def pg_init_db():
    print('DB_CREATED = ')
    print(DB_CREATED)
    if DB_CREATED == '1':
        return

    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE googleuser (
            id VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            profile_pic VARCHAR(255) NOT NULL
        )
        """,
    )
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()

        # DEBUG
        print('DEBUG: DB created')

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

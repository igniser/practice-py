from flask_login import UserMixin
import psycopg2

from db_postgre import pg_get_db


class UserPostgre(UserMixin):
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    @staticmethod
    def get(user_id):
        conn = pg_get_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM googleuser WHERE id = %s", (user_id,)
        )
        user = cur.fetchone()

        conn.commit()
        cur.close()

        if not user:
            return None

        user = UserPostgre(
            id_=user[0], name=user[1], email=user[2], profile_pic=user[3]
        )

        return user

    @staticmethod
    def create(id_, name, email, profile_pic):
        conn = None
        sql = """INSERT INTO googleuser(id, name, email, profile_pic)
                     VALUES(%s, %s, %s, %s);"""
        try:
            conn = pg_get_db()
            cur = conn.cursor()
            cur.execute(sql, (id_, name, email, profile_pic,))
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                # DEBUG
                print('DEBUG: user_postgre created.')
                conn.close()

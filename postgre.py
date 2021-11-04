
# script to manually create table
import psycopg2
import os

DATABASE_URL = os.environ['DB_URI']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()

s = "CREATE TABLE googleuser (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,email VARCHAR(255) NOT NULL,profile_pic VARCHAR(255) NOT NULL);"

cur.execute(s)
conn.commit()
cur.close()

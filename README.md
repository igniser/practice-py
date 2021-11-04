# practice-py

Practice creating a web app that authenticate users with Google OpenId Connect (OIDC)

Reference article 
https://realpython.com/flask-google-login/


Technologies used:
    See requirements.txt for dependency libraries used.

How to run this app:
0. Get a free postgresql database at heroku.  [Reference here](https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1#:~:text=1%20Log%20into%20Heroku.%20Navigate%20your%20browser%20to,PostgreSQL%20database%20from%20any%20PostgreSQL%20client%2C%20e.g.%20) 
   
    0.1 Set DB_URI environment variable with your heroku db credentials

    0.2 In a Python console with the DB_URI environment variable set correctly, manually create a table with script in postgre.py file.

1. Register your app with Google
2. Set the following environment variables

    set GOOGLE_CLIENT_ID=xxx

    set GOOGLE_CLIENT_SECRET=yyy

3. (optional) Generate an application key with " python -c 'import secrets; print(secrets.token_hex())' "
and set the following environment variable

    set SECRET_KEY=zzzz

4. Launch app with " python app.py "

5. In browser, go to "https://127.0.0.1:5000", assuming this application URL registered with Google.



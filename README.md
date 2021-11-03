# practice-py

Practice creating a web app that authenticate users with Google OpenId Connect (OIDC)

Reference article 
https://realpython.com/flask-google-login/


Technologies used:
    See requirements.txt for dependency libraries used.

How to run this app:
1. Register your app with Google
2. Set the following environment variables

    set GOOGLE_CLIENT_ID=xxx

    set GOOGLE_CLIENT_SECRET=yyy

3. (optional) Generate an application key with " python -c 'import secrets; print(secrets.token_hex())' "
and set the following environment variable

    set SECRET_KEY=zzzz

4. Launch app with " python app.py "

5. In browser, go to "https://127.0.0.1:5000", assuming this application URL registered with Google.



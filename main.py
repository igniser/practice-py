# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import flask

from flask import Flask
from flask import request
from flask import session

app = Flask(__name__)

# generate from " python -c 'import secrets; print(secrets.token_hex())' "
app.secret_key = '36f7c59ade623e406fae94775a9a883b234ca3835b2c2387794f89cbc7c4a110'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return flask.redirect('/')
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return flask.redirect('/')


@app.route('/')
def hello_world():
    # this is one way to output log messages
    # app.logger.error('inside helloworld()')

    # this is another way to output log message to console
    print('log with print - inside helloworld')

    if 'username' in session:
        return f'Logged in as {session["username"]}.  <a href="/logout">Logout</a>'
    return '''
            You are not logged in.  To login, click <a href="/login">Here</a>
        '''

if __name__ == '__main__':
   app.run()
from flask import Flask, jsonify, request, make_response
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] ='thisisthesecretkey'

@app.route('/admin')
def admin():
    return "Hello admin"

@app.route('/customer')
def customer():
    return "Hello customer"

@app.route('/employee')
def employee():
    return "Hello Employee"

@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({'user':auth.username, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=59)}), app.config['SECRET_KEY']

        return jsonify({'token':token.decode('UTF-8')})
    return make_response('Could not verify!', 401,{'www-Authenticate':'Basic realm-"Login Required"'})

    # return "Hello User"

if __name__ == '__main__':
    app.run(debug=True)
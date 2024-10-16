from flask import Flask, jsonify

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True

@app.route('/')
def home():
    return jsonify(message="Hello, World!")

@app.route('/api/data')
def data():
    return jsonify(data="Here is some data")

@app.route('/user/<username>')
def get_user(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return query


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

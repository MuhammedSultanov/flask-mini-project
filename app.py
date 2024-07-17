from flask import Flask, render_template, request
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from models import create_post, get_posts

app = Flask(__name__)
bcrypt = Bcrypt(app) 

CORS(app) #Secure againts XSS 

@app.route('/hello', methods=['GET', 'POST'])
def root():
    return f"Hello"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        create_post(name, hashed_password)

    posts = get_posts()

 
    return render_template('index.html', posts=posts)


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0', port='5000')
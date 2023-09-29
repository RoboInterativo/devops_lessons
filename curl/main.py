from flask import Flask,make_response,request
from base64 import standard_b64decode

from flask import Flask, redirect



from flask_httpauth import HTTPBasicAuth

from werkzeug.security import generate_password_hash, check_password_hash







app = Flask(__name__)



auth = HTTPBasicAuth()



users = {

    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")

}



@auth.verify_password
def verify_password(username, password):

    if username in users and  check_password_hash(users.get(username), password):

        return username



@app.route('/test_auth')
@auth.login_required
def index():

    return "<p>Hello, {}!</p>".format(auth.current_user())









@app.route('/test_redirect')
def hello():

    return redirect("/", code=302)



@app.route("/")
def hello_world():
    ua_string = request.user_agent
    return f"<p>Hello, World! {ua_string}</p>"

@app.route("/test_json", methods=['GET', 'POST'])
def test_json():
    if request.method == 'GET':

        return {
            "username": 'alexpricker',
            "theme": 'darl',
            "image": "3301.jpg",
        }

    if request.method == 'POST':   
            #data = request.get_json()
            return 'status'


@app.route('/images/<int:pid>.jpg')
def get_image(pid):
    if pid==3301:
        f=open("330164")
        s=f.read()
    else:
        f=open("67069072061066061")
        s=f.read()
    image_binary = standard_b64decode(s)
    response = make_response(image_binary)
    response.headers.set('Content-Type', 'image/jpeg')
    response.headers.set(
        'Content-Disposition', 'attachment', filename='%s.jpg' % pid)
    return response

@app.route('/method', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':

        return "Use method GET"
    if request.method == 'POST':

            return "Use method POST"

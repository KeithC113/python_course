from app import flask_app 

@flask_app.route('/')
def index():
    return "Hello World!"

@flask_app.route('/<name>')
def index_name(name):
    return f"Hello {name}!"

@flask_app.route('/users/admin')
def users():
    return "List of users"
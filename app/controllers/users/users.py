from app import app 

@app.route('/users')
def hello_world():
    return 'Hello, World!'
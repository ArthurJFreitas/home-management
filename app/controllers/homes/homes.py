from app import app 
from flask import request

@app.route('/homes/<home_id>', methods = ['GET', 'POST'])
def home(home_id):
    req_data = request.get_json()

    if request.method == 'GET':
            return home_id
    if request.method == 'POST':
            return req_data["test"]
          
 

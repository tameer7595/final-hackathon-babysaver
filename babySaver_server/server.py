from flask import Flask, request, Response, jsonify
# from flask_mongoengine import MongoEngine

import warnings
warnings.simplefilter("ignore", DeprecationWarning)

# Initialize the Flask application
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    "db": "myapp",
}


# db = MongoEngine(app)

@app.route('/')
def start():
    return "Hello To My Server"


# route http posts to this method
@app.route('/api/pi', methods=['POST'])
def pi():
    r = request
    car_license = r.data.decode("utf-8")
    print(f"from pi: {car_license}")
    return jsonify({'ip': request.remote_addr}), 200


# route http posts to this method
@app.route('/api/web_page', methods=['POST'])
def web_page():
    r = request
    car_license = r.data.decode("utf-8")
    print(f"from web page: {car_license}")
    return jsonify({'ip': request.remote_addr}), 200


# start flask app
app.run(debug=True, host='0.0.0.0')

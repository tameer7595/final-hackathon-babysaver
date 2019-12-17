from flask import Flask, request, Response, jsonify
import flask_mongoengine
import mongoengine as me
import warnings
from Dealer import dealer

warnings.simplefilter("ignore", DeprecationWarning)

# Initialize the Flask application

app = Flask(__name__)
app.config.from_object(__name__)

app.config['MONGODB_SETTINGS'] = {'DB': 'babysaver'}

db = flask_mongoengine.MongoEngine()
db.init_app(app)


class User(me.Document):
    car_number = me.StringField(max_length=20)
    phone_numbers = me.StringField(max_length=200)


@app.route('/')
def start():
    return "Hello To My Server"


# route http posts to this method
@app.route('/api/pi', methods=['POST'])
def pi():
    r = request
    car_license = r.data.decode("utf-8")

    try:
        phone_numbers = next(User.objects(car_number__contains=car_license)).phone_number.split(',')

        for phone in phone_numbers:
            dealer.send_message(phone)
            dealer.phone_call(phone)
    finally:
        pass

    return jsonify({'ip': request.remote_addr}), 200


# route http posts to this method
@app.route('/api/web_page', methods=['POST'])
def web_page():
    r = request
    data = r.data.decode("utf-8")
    spliting_data = data.split(',')
    car_license = spliting_data[0]
    phone_num = spliting_data[1]
    try:
        User.objects(car_number__contains=car_license).update(
            set__phone_numbers=next(User.objects(car_number__contains=car_license)).phone_numbers + ',' + phone_num)
    finally:
        User(car_number=car_license, phone_numbers=phone_num).save()

    print(f"from web page: {car_license}")
    return jsonify({'ip': request.remote_addr}), 200


# start flask app
app.run(debug=True, host='0.0.0.0')

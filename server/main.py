import csv
import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

with open('./countrylist.csv') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  for line in reader:
    ALL_COUNTRIES = line

COUNTRIES = [
    {
        'id': uuid.uuid4().hex,
        'name': 'Malaysia',
        'vaccinated': 'Yes',
        'non_vaccinated': 'Yes',
        'airportCode': 'KUL'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Taiwan',
        'vaccinated': 'Yes, with 14 day quarantine',
        'non_vaccinated': 'No',
        'airportCode': 'TPE'
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Brunei',
        'vaccinated': 'Yes',
        'non_vaccinated': 'Yes, with 14 day quarantine',
        'airportCode': 'BWN'
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

def remove_country(country_id):
    for country in COUNTRIES:
        if country['id'] == country_id:
            COUNTRIES.remove(country)
            return True
    return False

@app.route('/countrylist', methods=['GET'])
def country_list():
  response_object = {
    'status': 'success',
    'country_list': ALL_COUNTRIES
    }
  return jsonify(response_object)

@app.route('/countries', methods=['GET', 'POST'])
def all_countrys():
    response_object = {'status': 'success'}

    if request.method == 'GET':
        COUNTRIES.sort(key=lambda x: x['name'])
        response_object['countries'] = COUNTRIES

    if request.method == 'POST':
        post_data = request.get_json()
        COUNTRIES.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'vaccinated': post_data.get('vaccinated'),
            'non_vaccinated': post_data.get('non_vaccinated')
        })
        response_object['message'] = 'Country added!'
    
    return jsonify(response_object)

@app.route('/countries/<country_id>', methods=['PUT', 'DELETE'])
def single_country(country_id):
    response_object = {'status': 'success'}

    if request.method == 'PUT':
        post_data = request.get_json()
        remove_country(country_id)
        COUNTRIES.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'vaccinated': post_data.get('vaccinated'),
            'non_vaccinated': post_data.get('non_vaccinated')
        })
        response_object['message'] = 'Country updated!'

    if request.method == 'DELETE':
        remove_country(country_id)
        response_object['message'] = 'Country removed!'

    return jsonify(response_object)

# catch
@app.route('/', methods=['GET'])
def catch_index():
    return jsonify('Welcome to the backend!')

if __name__ == '__main__':
    app.run()

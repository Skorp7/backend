from flask import Flask
from flask_restx import Api, Resource
from flask_cors import CORS
import fetch_from_museovirasto
import geojson

app = Flask(__name__)
api = Api(app)

CORS(app)

@api.route('/api/helloworld')
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

@api.route('/api/healthcheck')
class HealthCheck(Resource):
    def get(self):
        return {'status': 'ok'}

@api.route('/api/updatedata')
class updatedata(Resource):
    def get(self):
        fetch_from_museovirasto.save_wrecks_geojson('data')
        return {'status':'update done'}

@api.route('/api/getdata')
class getdata(Resource):
    def get(self):
        f = open('data/wreckdata.json')
        return geojson.load(f)

if __name__ == '__main__':
    app.run(debug=True)

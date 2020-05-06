from flask_restful import Resource


class StaticData(Resource):
    def get(self):
        return {'data1': 1, 'data2': 2}

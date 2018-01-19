from flask_restful import Resource, reqparse


class Parsing(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('param2', type=str, required=False, help="No param2 provided.", location='json')
        super(Parsing, self).__init__()

    def get(self, param1):
        return {'param1': param1}

    def post(self, param1):
        args = self.parser.parse_args()
        return {'param2': args['param2'], 'param1': param1}

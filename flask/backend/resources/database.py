from flask_restful import Resource, reqparse


class Database(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        super(Database, self).__init__()

    def get(self):
        # TODO: Implement database example
        pass

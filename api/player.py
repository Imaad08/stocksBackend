from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building

from model.players import Player

# Change variable name and API name and prefix
player_api = Blueprint('player_api', __name__,
                   url_prefix='/api/players')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(player_api)

class PlayerAPI:     
    class Action(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # validate uid
            uid = body.get('uid')
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            # look for password and tokens
            password = body.get('password')
            tokens = body.get('tokens')

            ''' #1: Key code block, setup PLAYER OBJECT '''
            po = Player(name=name, 
                        uid=uid,
                        tokens=tokens)
            
            ''' Additional garbage error checking '''
            # set password if provided
            if password is not None:
                po.set_password(password)            
            
            ''' #2: Key Code block to add user to database '''
            # create player in database
            player = po.create()
            # success returns json of player
            if player:
                return jsonify(player.read())
            # failure returns error
            return {'message': f'Processed {name}, either a format error or User ID {uid} is duplicate'}, 210

        def get(self):
            players = Player.query.all()    # read/extract all players from database
            json_ready = [player.read() for player in players]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

        def put(self):
            body = request.get_json() # get the body of the request
            uid = body.get('uid') # get the UID (Know what to reference)
            data = body.get('data')
            player = Player.query.get(uid) # get the player (using the uid in this case)
            player.update(data)
            return f"{player.read()} Updated"

        def delete(self):
            body = request.get_json()
            uid = body.get('uid')
            player = Player.query.get(uid)
            player.delete()
            return f"{player.read()} Has been deleted"


    # building RESTapi endpoint, method distinguishes action
    api.add_resource(Action, '/')

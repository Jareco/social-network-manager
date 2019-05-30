import json
from flask import Flask, Response, request, abort
from Connections.MysqlConnection import MysqlConnection
from Handlers.SocialNetworkHandler import SocialNetworkHandler
from Handlers.UserHandler import UserHandler

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

database_connection = MysqlConnection();

@app.route("/api/networks", methods=['GET', 'POST'])
def handle_networks():
    handler = SocialNetworkHandler(database_connection);
    if request.method == 'GET':
        networks = handler.get();
        return Response(json.dumps(networks), status=200);
    else:
        network_to_add = request.json;
        handler.add(network_to_add['url'], network_to_add['design'], network_to_add['name']);     
        return Response(status=200);


@app.route("/api/networks/delete", methods=['POST'])
def delete_network():
    handler = SocialNetworkHandler(database_connection);
    network_to_delete = request.json;
    handler.delete_by_url(network_to_delete['url']);
    return Response(status=200);

@app.route("/api/users", methods=['GET', 'POST'])
def handle_users():
    handler = UserHandler(database_connection);
    if request.method == 'GET':
        users = handler.get();
        return Response(json.dumps(users), status=200);
    else:
        user_to_add = request.json;
        handler.add(user_to_add['email'], user_to_add['firstName'], user_to_add['email'], user_to_add['lastName'], user_to_add['url']);
        return Response(status=200);

@app.route("/api/users/delete", methods=['POST'])
def delete_user():
    handler = UserHandler(database_connection);
    user_to_delete = request.json;
    handler.delete_by_email(user_to_delete['email']);
    return Response(status=200);


    



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

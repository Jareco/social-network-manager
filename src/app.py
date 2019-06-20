import json
from flask import Flask, Response, request, abort
from Connections.MysqlConnection import MysqlConnection
from Handlers.SocialNetworkHandler import SocialNetworkHandler
from Handlers.UserHandler import UserHandler
from Handlers.ProfileHandler import ProfileHandler
from Handlers.WorkerHandler import WorkerHandler
from Handlers.DeveloperHandler import DeveloperHandler
from Handlers.ManagerHandler import ManagerHandler
from Migrator import migrator
import pymongo
from bson.json_util import dumps




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

@app.route("/api/networks/search", methods=['POST'])
def find_networks():
    handler = SocialNetworkHandler(database_connection);
    url_to_search = request.json['valueToSearch'];
    networks = handler.find_by_url(url_to_search);
    return Response(json.dumps(networks), status=200);

@app.route("/api/users", methods=['GET', 'POST'])
def handle_users():
    handler = UserHandler(database_connection);
    if request.method == 'GET':
        users = handler.get();
        return Response(json.dumps(users), status=200);
    else:
        user_to_add = request.json;
        handler.add(user_to_add['email'], user_to_add['firstName'], user_to_add['lastName'], user_to_add['url']);
        return Response(status=200);

@app.route("/api/users/delete", methods=['POST'])
def delete_user():
    handler = UserHandler(database_connection);
    user_to_delete = request.json;
    handler.delete_by_email(user_to_delete['email']);
    return Response(status=200);

@app.route("/api/users/search", methods=['POST'])
def find_users():
    handler = UserHandler(database_connection);
    email_to_search = request.json['valueToSearch'];
    users = handler.find_by_email(email_to_search);
    return Response(json.dumps(users), status=200);

@app.route("/api/profiles", methods=['GET', 'POST'])
def handle_profiles():
    handler = ProfileHandler(database_connection);
    if request.method == 'GET':
        profiles = handler.get();
        return Response(json.dumps(profiles, indent=4, sort_keys=True, default=str), status=200);
    else:
        profile_to_add = request.json;
        handler.add(profile_to_add['birthdate'], profile_to_add['city'], profile_to_add['telnumber'], profile_to_add['education'], profile_to_add['photos'], profile_to_add['email']);
        return Response(status=200);
    
@app.route("/api/profiles/delete", methods=['POST'])
def delete_profile():
    handler = ProfileHandler(database_connection);
    profile_to_delete = request.json;
    handler.delete_by_id(profile_to_delete['id']);
    return Response(status=200);

@app.route("/api/profiles/search", methods=['POST'])
def find_profiles():
    handler = ProfileHandler(database_connection);
    email_to_search = request.json['valueToSearch'];
    profiles = handler.find_by_email(email_to_search);
    return Response(json.dumps(profiles, indent=4, sort_keys=True, default=str), status=200);

@app.route("/api/profiles/search/double", methods=['GET'])
def find_double_profiles():
    handler = ProfileHandler(database_connection);
    profiles = handler.find_double();
    return Response(json.dumps(profiles, indent=4, sort_keys=True, default=str), status=200);

@app.route("/api/workers", methods=['GET', 'POST'])
def handle_workers():
    handler = WorkerHandler(database_connection);
    if request.method == 'GET':
        workers = handler.get();
        return Response(json.dumps(workers, indent=4, sort_keys=True, default=str), status=200);
    else:
        worker_to_add = request.json;
        handler.add(worker_to_add['pernr'], worker_to_add['firstName'], worker_to_add['lastName'], worker_to_add['birthdate'], worker_to_add['url'], worker_to_add['since']);
        return Response(status=200);

@app.route("/api/workers/delete", methods=['POST'])
def delete_worker():
    handler = WorkerHandler(database_connection);
    worker_to_delete = request.json;
    handler.delete_by_pernr(worker_to_delete['pernr']);
    return Response(status=200);

@app.route("/api/workers/search", methods=['POST'])
def find_workers():
    handler = WorkerHandler(database_connection);
    first_name_to_search = request.json['valueToSearch'];
    workers = handler.find_by_first_name(first_name_to_search);
    return Response(json.dumps(workers, indent=4, sort_keys=True, default=str), status=200);


@app.route("/api/developers", methods=['GET', 'POST'])
def handler_developers():
    handler = DeveloperHandler(database_connection);
    if request.method == 'GET':
        developers = handler.get();
        return Response(json.dumps(developers), status=200);
    else:
        developer_to_add = request.json;
        handler.add(developer_to_add['developernr'], developer_to_add['nickname'], developer_to_add['login'], developer_to_add['password'], developer_to_add['pernr']);
        return Response(status=200);


@app.route("/api/developers/delete", methods=['POST'])
def delete_developer():
    handler = DeveloperHandler(database_connection);
    developer_to_delete = request.json;
    handler.delete_by_developernr(developer_to_delete['developernr']);
    return Response(status=200);

@app.route("/api/developers/search", methods=['POST'])
def find_developers():
    handler = DeveloperHandler(database_connection);
    developer_number_to_search = request.json['valueToSearch'];
    developers = handler.find_by_developer_number(developer_number_to_search);
    return Response(json.dumps(developers), status=200);

@app.route("/api/developers/details/<developernr>", methods=['GET'])
def get_developer_details(developernr):
    handler = DeveloperHandler(database_connection);
    developers = handler.get_developer_details(developernr);
    return Response(json.dumps(developers, indent=4, sort_keys=True, default=str), status=200);

@app.route("/api/managers", methods=['GET', 'POST'])
def handler_managers():
    handler = ManagerHandler(database_connection);
    if request.method == 'GET':
        managers = handler.get();
        return Response(json.dumps(managers), status=200);
    else:
        manager_to_add = request.json;
        handler.add(manager_to_add['managernr'], manager_to_add['emailM'], manager_to_add['telnumberM'], manager_to_add['pernr']);
        return Response(status=200);

@app.route("/api/managers/delete", methods=['POST'])
def delete_manager():
    handler = ManagerHandler(database_connection);
    manager_to_delete = request.json;
    handler.delete_by_managernr(manager_to_delete['managernr']);
    return Response(status=200);

@app.route("/api/managers/search", methods=['POST'])
def find_managers():
    handler = ManagerHandler(database_connection);
    manager_number_to_search = request.json['valueToSearch'];
    managers = handler.find_by_manager_number(manager_number_to_search);
    return Response(json.dumps(managers), status=200);

@app.route("/api/migrate", methods=['GET'])
def migrate_data():
    migrator.start_migration();
    return Response(json.dumps({'status': 'OK'}), status=200);

@app.route("/api/mongo/networks", methods=['GET', 'POST'])
def handle_networks_mongo():
    mongodb_client = pymongo.MongoClient("mongodb://admin:imse@mongo:27017/");
    mydb = mongodb_client["imse_database"];
    social_network_collection = mydb["socialNetwork"];
    if request.method == 'GET':
        social_networks_json = dumps(social_network_collection.find());
        return Response(social_networks_json, status=200);
    if request.method == 'POST':
        network_to_add = request.json;
        last_network = social_network_collection.find_one(sort=[( '_id', pymongo.DESCENDING )])
        last_id = last_network['_id'];
        network_to_add.update({'_id': last_id + 1});
        social_network_collection.insert_one(network_to_add);
        return Response(status=200);


@app.route("/api/mongo/networks/delete", methods=['POST'])
def delete_network_mongo():
    network_to_delete = request.json;
    mongodb_client = pymongo.MongoClient("mongodb://admin:imse@mongo:27017/");
    mydb = mongodb_client["imse_database"];
    social_network_collection = mydb["socialNetwork"];
    social_network_collection.delete_many({'url': network_to_delete['url']});
    return Response(status=200);


@app.route("/api/mongo/networks/search", methods=['POST'])
def find_networks_mongo():
    url_to_search = request.json['valueToSearch'];
    mongodb_client = pymongo.MongoClient("mongodb://admin:imse@mongo:27017/");
    mydb = mongodb_client["imse_database"];
    social_network_collection = mydb["socialNetwork"];
    social_networks_json = dumps(social_network_collection.find({'url': {'$regex': '' + url_to_search + ''}}));
    return Response(social_networks_json, status=200);

@app.route("/api/mongo/developers", methods=['GET'])
def handler_developers_mongo():
    mongodb_client = pymongo.MongoClient("mongodb://admin:imse@mongo:27017/");
    mydb = mongodb_client["imse_database"];
    worker_collection = mydb["worker"];
    developers = dumps(worker_collection.find({'type': 'developer'}, {'developer': 1, 'pernr': 1}));
    return Response(developers, status=200);

@app.route("/api/mongo/developers/details/<workerid>", methods=['GET'])
def get_developer_details_mongo(workerid):
    mongodb_client = pymongo.MongoClient("mongodb://admin:imse@mongo:27017/");
    mydb = mongodb_client["imse_database"];
    worker_collection = mydb["worker"];
    worker = worker_collection.find_one({'_id': int(workerid)});
    response = {'developernr': worker['developer']['developernr'], 'socialNetwork': worker['url'], 'employementDate': worker['since']};
    return Response(json.dumps(response, indent=4, sort_keys=True, default=str), status=200);


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

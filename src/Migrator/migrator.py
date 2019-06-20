import json
import mysql.connector
import pymongo


class MysqlConnection:    
    def __init__(self):
        while True:
            try:
                self.mydb = mysql.connector.connect(user='imse',
                                                    database='imse',
                                                    password="imsepwd",
                                                    host='mariadb'); # change
                break;
            except:
                continue;
    
    
    # All actions, which only read from database
    def read_action(self, sqlstatement):
        mycursor = self.mydb.cursor(dictionary=True);
        mycursor.execute(sqlstatement);
        result = mycursor.fetchall();
        return result;

def start_migration():
    
    mysql_client = MysqlConnection();
    print("Connected to mysql");


    mongodb_client = None;
    while True:
        try:
            mongodb_client = pymongo.MongoClient("mongodb://admin:imse@mongo:27017/") #change host.
            break;
        except:
            continue;

    print("Connected to mongodb");
    mydb = mongodb_client["imse_database"];
    social_network_collection = mydb["socialNetwork"];
    user_collection = mydb["user"];
    worker_collection = mydb["worker"];
    print("Created collections");

    print("Starting data migration");

    print("Starting migration of social networks");
    social_networks = mysql_client.read_action("SELECT * FROM socialNetwork");
    for index, social_network in enumerate(social_networks):
        social_network.update({'_id': index + 1});
        social_network_collection.insert_one(social_network);
    print("Social networks migration is done");

    print("Starting migration of users");
    # Migrate users
    users = mysql_client.read_action("SELECT * FROM user");
    for index, user in enumerate(users):
        user.update({'_id': index + 1});
        url = user['url'];
        social_network = social_network_collection.find_one({'url' : url});
        user.pop('url', None);
        user.update({'socialNetwork': social_network['_id']});
        user_collection.insert_one(user);
    print("Users migration is done");

    print("Starting embeding of profile in users");
    # Embed profiles in user
    profiles = mysql_client.read_action("SELECT * FROM profile");
    for index, profile in enumerate(profiles):
        profile.update({'_id' : index + 1});
        user = user_collection.find_one({'email': profile['email']});
        profile_json = json.dumps(profile, indent=4, sort_keys=True, default=str);
        profile = json.loads(profile_json);
        profile.pop('id', None);
        email_to_find = profile['email'];
        profile.pop('email', None)
        user.update({'profile': profile});
        user_collection.update_one({'email': email_to_find}, { "$set": user });
    print("Embeding profile in users is done");

    # Find friends of users
    print("Starting migration of friends of users");
    for index, user in enumerate(user_collection.find()):
        sql = f"SELECT email2 AS email FROM friendOf WHERE email1 = '{user['email']}'";
        friends = mysql_client.read_action(sql);
        ids_of_friends = [];
        for friend in friends:
            email_of_friend = friend['email'];
            friend_from_mongodb = user_collection.find_one({'email': email_of_friend});
            ids_of_friends.append(friend_from_mongodb['_id']);
        user.update({'friends': ids_of_friends});
        user_collection.update_one({'email': user['email']}, { "$set": user });

    for index, user in enumerate(user_collection.find()):
        sql = f"SELECT email1 AS email FROM friendOf WHERE email2 = '{user['email']}'";
        friends = mysql_client.read_action(sql);
        ids_of_friends = [];
        for friend in friends:
            email_of_friend = friend['email'];
            friend_from_mongodb = user_collection.find_one({'email': email_of_friend});
            ids_of_friends.append(friend_from_mongodb['_id']);
        merged_list = user['friends'] + ids_of_friends;
        user['friends'] = merged_list;
        user_collection.update_one({'email': user['email']}, { "$set": user });
    print("Migration of friends is done");

    # Migration workers
    print("Starting migration of workers");
    workers = mysql_client.read_action("SELECT * FROM worker");

    for index, worker in enumerate(workers):
        worker.update({'_id' : index + 1});
        worker_json = json.dumps(worker, indent=4, sort_keys=True, default=str);
        worker = json.loads(worker_json);
        worker_collection.insert_one(worker);
    print("Migration of workers is done");

    # Embeding developers
    print("Starting embeding developers");

    developer_sql = "SELECT developer.developernr, developer.nickname, developer.login, developer.password, developer.pernr FROM developer INNER JOIN worker ON developer.pernr = worker.pernr";
    developers = mysql_client.read_action(developer_sql);

    for index, developer in enumerate(developers):
        worker = worker_collection.find_one({'pernr': developer['pernr']});
        developer.pop('pernr', None);
        developer.update({'_id' : index + 1});
        worker.update({'developer': developer});
        worker.update({'type': 'developer'});
        worker_collection.update_one({'pernr': worker['pernr']}, { "$set": worker });

    print("Embeding developers is done");


    # Embeding managers
    print("Starting embeding managers");
    manager_sql = "SELECT manager.pernr, manager.managernr, manager.emailM, manager.telnumberM FROM manager INNER JOIN worker ON manager.pernr = worker.pernr";
    managers = mysql_client.read_action(manager_sql);

    for index, manager in enumerate(managers):
        worker = worker_collection.find_one({'pernr': manager['pernr']});
        manager.pop('pernr', None);
        manager.update({'_id': index + 1});
        worker.update({'manager': manager});
        worker.update({'type': 'manager'});
        worker_collection.update_one({'pernr': worker['pernr']}, { "$set": worker });
    print("Embeding managers is done");

    print("Migration is done");



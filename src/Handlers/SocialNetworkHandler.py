
class SocialNetworkHandler:
    
    def __init__(self, database_connection):
        self.db_conn = database_connection;
        
    def get(self):
        networks = self.db_conn.read_action("SELECT * FROM socialNetwork");
        return networks;
    
    def add(self, url, design, name):
        sql = f"INSERT INTO socialNetwork (url, design, name) VALUES ('{url}', '{design}', '{name}')";
        self.db_conn.write_action(sql);
    
    def delete_by_url(self, url):
        sql = f"DELETE FROM socialNetwork WHERE url = '{url}'";
        self.db_conn.write_action(sql);
        

        
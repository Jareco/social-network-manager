
class UserHandler:
    
    def __init__(self, database_connection):
        self.db_conn = database_connection;
        
    def get(self):
        networks = self.db_conn.read_action("SELECT * FROM user");
        return networks;
    
    def add(self, email, first_name, last_name, url):
        sql = f"INSERT INTO user (email, firstName, lastName, url) VALUES ('{email}', '{first_name}', '{last_name}', '{url}')";
        self.db_conn.write_action(sql);
    
    def delete_by_email(self, email):
        sql = f"DELETE FROM user WHERE email = '{email}'";
        self.db_conn.write_action(sql);
        

        
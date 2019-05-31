
class UserHandler:
    
    def __init__(self, database_connection):
        self.db_conn = database_connection;
        
    def get(self):
        users = self.db_conn.read_action("SELECT * FROM user");
        return users;
    
    def add(self, email, first_name, last_name, url):
        sql = f"INSERT INTO user (email, firstName, lastName, url) VALUES ('{email}', '{first_name}', '{last_name}', '{url}')";
        self.db_conn.write_action(sql);
    
    def delete_by_email(self, email):
        sql = f"DELETE FROM user WHERE email = '{email}'";
        self.db_conn.write_action(sql);

    def find_by_email(self, email_to_search):
        sql = "SELECT * FROM user WHERE email like '%" + email_to_search + "%'";
        users = self.db_conn.read_action(sql);
        return users;
        

        
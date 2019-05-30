
class ProfileHandler:
    
    def __init__(self, database_connection):
        self.db_conn = database_connection;
        
    def get(self):
        networks = self.db_conn.read_action("SELECT * FROM profile");
        return networks;
    
    def add(self, birthdate, city, telnumber, education, photos, email):
        sql = f"INSERT INTO profile (birthdate, city, telnumber, education, photos, email) VALUES ('{birthdate}', '{city}', '{telnumber}', '{education}', '{photos}', '{email}')";
        self.db_conn.write_action(sql);
    
    def delete_by_id(self, id):
        sql = f"DELETE FROM profile WHERE id = '{id}'";
        self.db_conn.write_action(sql);
        

        
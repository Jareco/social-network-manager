
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
        
    def find_by_email(self, email_to_search):
        sql = "SELECT * FROM profile WHERE email like '%" + email_to_search + "%'";
        profiles = self.db_conn.read_action(sql);
        return profiles;

    def find_double(self):
        sql = "SELECT * from profile GROUP BY email HAVING COUNT(*) > 1)";
        profiles = self.db_conn.read_action(sql);
        return profiles;     

        
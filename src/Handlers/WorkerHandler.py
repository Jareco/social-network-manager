
class WorkerHandler:
    
    def __init__(self, database_connection):
        self.db_conn = database_connection;
        
    def get(self):
        workers = self.db_conn.read_action("SELECT * FROM worker");
        return workers;
    
    def add(self, pernr, first_name, last_name, birthdate, url, since):
        sql = f"INSERT INTO worker (pernr, firstName, lastName, birthdate, url, since) VALUES ('{pernr}', '{first_name}', '{last_name}','{birthdate}', '{url}', '{since}')";
        self.db_conn.write_action(sql);
    
    def delete_by_pernr(self, pernr):
        sql = f"DELETE FROM worker WHERE pernr = '{pernr}'";
        self.db_conn.write_action(sql);
    
    def find_by_first_name(self, first_name_to_search):
        sql = "SELECT * FROM worker WHERE firstName like '%" + first_name_to_search + "%'";
        workers = self.db_conn.read_action(sql);
        return workers;
     

        
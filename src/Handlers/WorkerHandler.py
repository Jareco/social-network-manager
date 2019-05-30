
class WorkerHandler:
    
    def __init__(self, database_connection):
        self.db_conn = database_connection;
        
    def get(self):
        workers = self.db_conn.read_action("SELECT * FROM worker");
        return workers;
    
    def add(self, pernr, first_name, last_name, birthdate, url):
        sql = f"INSERT INTO worker (pernr, firstName, lastName, birthdate, url) VALUES ('{pernr}', '{first_name}', '{last_name}','{birthdate}', '{url}')";
        self.db_conn.write_action(sql);
    
    def delete_by_pernr(self, pernr):
        sql = f"DELETE FROM worker WHERE pernr = '{pernr}'";
        self.db_conn.write_action(sql);
     

        
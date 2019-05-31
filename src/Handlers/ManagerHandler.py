
class ManagerHandler:
    
    def __init__(self, database_connection):
        self.db_conn = database_connection;
        
    def get(self):
        managers = self.db_conn.read_action("SELECT * FROM manager");
        return managers;
    
    def add(self, managernr, email_m, telnumber_m, pernr):
        sql = f"INSERT INTO manager (managernr, emailM, telnumberM, pernr) VALUES ('{managernr}', '{email_m}', '{telnumber_m}', '{pernr}')";
        self.db_conn.write_action(sql);
    
    def delete_by_managernr(self, managernr):
        sql = f"DELETE FROM manager WHERE managernr = '{managernr}'";
        self.db_conn.write_action(sql);
    
    def find_by_manager_number(self, manager_number_to_search):
        sql = "SELECT * FROM manager WHERE managernr like '%" + manager_number_to_search + "%'";
        managers = self.db_conn.read_action(sql);
        return managers;

        

        
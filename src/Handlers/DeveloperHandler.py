
class DeveloperHandler:
    
    def __init__(self, database_connection):
        self.db_conn = database_connection;
        
    def get(self):
        developers = self.db_conn.read_action("SELECT * FROM developer");
        return developers;
    
    def add(self, developernr, nickname, login, password, pernr):
        sql = f"INSERT INTO developer (developernr, nickname, login, password, pernr) VALUES ('{developernr}', '{nickname}', '{login}', '{password}', '{pernr}')";
        self.db_conn.write_action(sql);
    
    def delete_by_developernr(self, developernr):
        sql = f"DELETE FROM developer WHERE developernr = '{developernr}'";
        self.db_conn.write_action(sql);

    def find_by_developer_number(self, developer_number_to_search):
        sql = "SELECT * FROM developer WHERE developernr like '%" + developer_number_to_search + "%'";
        developers = self.db_conn.read_action(sql);
        return developers;
    
    def get_developer_details(self, developernr):
        sql ="SELECT developer.developernr AS developernr, worker.since AS employementDate, socialNetwork.url AS socialNetwork FROM developer INNER JOIN worker ON developer.pernr = worker.pernr INNER JOIN socialNetwork ON worker.url = socialNetwork.url WHERE developer.developernr = " + str(developernr);
        developers = self.db_conn.read_action(sql);
        return developers;
        

        
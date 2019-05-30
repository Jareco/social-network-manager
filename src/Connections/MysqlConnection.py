import mysql.connector

class MysqlConnection:
    
    def __init__(self):
        self.mydb = mysql.connector.connect(user='imse',
                                            database='imse',
                                            password="imsepwd",
                                            host='mariadb');
    
    
    # All actions, which only read from database
    def read_action(self, sqlstatement):
        mycursor = self.mydb.cursor(dictionary=True);
        mycursor.execute(sqlstatement);
        result = mycursor.fetchall();
        return result;
    
    # All actions, which need to write in the database
    def write_action(self, sqlstatement):
        mycursor = self.mydb.cursor(dictionary=True);
        mycursor.execute(sqlstatement);
        self.mydb.commit();


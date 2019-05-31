import mysql.connector


mydb = mysql.connector.connect(user='imse',
                                database='imse',
                                password="imsepwd",
                                host='localhost');

f1 = open(".././Databank_project/1549702_Romanov_create.sql", "r");
tables_creator = f1.read();
mycursor = mydb.cursor();
results = mycursor.execute(tables_creator, multi=True);
try:
    for cur in results:
        print('cursor:', cur)
        if cur.with_rows:
            print('result:', cur.fetchall())
except:
    print("Exception");
mydb.commit();

## Data generating:

## Social Network:
try:
    sql1 = "INSERT INTO socialNetwork VALUES ('http://ok.ru','Orange','OK')";
    mycursor = mydb.cursor();
    mycursor.execute(sql1);
    mydb.commit();
except:
    print("Impossible to add social network");

## User
for i in range (1, 300):
    try:
        s = str(i);
        sql2 = "INSERT INTO user VALUES ('email" + s + "@gmail.com','Name" + s + "','Last Name" + s + "','http://ok.ru')";
        mycursor = mydb.cursor();
        mycursor.execute(sql2);
    except:
        print(sql2);
        print("Impossible to add users");
mydb.commit();

mydb.close();




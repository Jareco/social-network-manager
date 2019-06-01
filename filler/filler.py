import mysql.connector


while True:
    try:
        mydb = mysql.connector.connect(user='root',
                                        database='imse',
                                        password="root",
                                        host='mariadb');
        break;
    except:
        continue;

f1 = open("/filler/create.sql", "r");
tables_creator = f1.read();
mycursor = mydb.cursor();
results = mycursor.execute(tables_creator, multi=True);
isFirstEntry = True; # Prevention of double inserting
try:
    for cur in results:
        print('cursor:', cur)
        if cur.with_rows:
            print('result:', cur.fetchall())
        isFirstEntry = False;
except:
    if (isFirstEntry):
        exit();
    print("Exception");
mydb.commit();

print("Tables created");

## Data generating:

## Social Network:
try:
    sql1 = "INSERT INTO socialNetwork VALUES ('http://ok.at','Orange','OK')";
    mycursor = mydb.cursor();
    mycursor.execute(sql1);
    mydb.commit();
except:
    print("Impossible to add social network");

print("Social Network inserted");

## User
for i in range (1, 300):
    try:
        s = str(i);
        sql2 = "INSERT INTO user VALUES ('email" + s + "@gmail.com','Name" + s + "','Last Name" + s + "','http://ok.at')";
        mycursor = mydb.cursor();
        mycursor.execute(sql2);
    except:
        print("Impossible to add users");
mydb.commit();

print("Users inserted");

## Friend of
j = 2;
for i in range(1, 100):
    s = str(i);
    p = str(j);
    try:
        s = str(i);
        sql3 = "INSERT INTO friendOf VALUES ('email" + s + "@gmail.com','email" + p + "@gmail.com')";
        mycursor = mydb.cursor();
        mycursor.execute(sql3);
    except:
        print("Impossible to add friendOf");
    j = j + 1;

mydb.commit();

print("FriendsOf inserted");

## Profile
telephone_number_ending = 3000;
for i in range(1, 300):
    try:
        n = str(telephone_number_ending);
        s = str(i);
        sql4 = "INSERT INTO profile (birthdate,city,telnumber,education,photos,email)VALUES ('1995-07-11','Vienna',0660123" + n + ",'University Vienna', 5, 'email" + s + "@gmail.com')";
        mycursor = mydb.cursor();
        mycursor.execute(sql4);
    except:
        print("Impossible to add profile");
mydb.commit();

print("Profiles inserted");

## Worker
for i in range(1, 300):
    try:
        s = str(i);
        sql5 = "INSERT INTO worker VALUES(" + s + ", 'Max" + s + "', 'Gruber" + s + "', '1980-07-11','http://ok.at','2012-05-13')";
        mycursor = mydb.cursor();
        mycursor.execute(sql5);
    except:
        print("Impossible to add Worker");
mydb.commit();

print("Workers inserted");


## Developer
developer_number = 3001;
for i in range(1, 150):
    try:
        s = str(developer_number);
        p = str(i);
        sql6 = "INSERT INTO developer VALUES(" + s + ", 'Nickname" + p + "', 'a" + s + "2', 't" + p + "s35d'," + p + ")";
        mycursor = mydb.cursor();
        mycursor.execute(sql6);
    except:
        print("Impossible to add Developer");
    developer_number = developer_number + 1;
mydb.commit();

print("Developers inserted");

## Manager
manager_number = 500;
for i in range(150, 300):
    try:
        s = str(manager_number);
        p = str(i);
        sql7 = "INSERT INTO manager VALUES(" + s + ", 'bbb" + p + "@ggg.at', 0676234" + p + "," + p + ")";
        mycursor = mydb.cursor();
        mycursor.execute(sql7);
    except:
        print("Impossible to add Developer");
    manager_number = manager_number + 1;
mydb.commit();

print("Mangers inserted");

mydb.close();

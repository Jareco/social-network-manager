
INSERT INTO socialNetwork VALUES ('http://vk.com','blaue Farbe','VK');
INSERT INTO user VALUES ('afd@dfs.at', 'Mark', 'Lehner','http://vk.com');
INSERT INTO user VALUES ('aa@dfs.at', 'Alfred', 'Muster','http://vk.com');
INSERT INTO friendOf (email1, email2) VALUES ('afd@dfs.at','aa@dfs.at');
INSERT INTO profile (birthdate,city,telnumber,education,photos,email)VALUES ('1995-01-23','Wien',06601234242,'Uni Wien', 5, 'afd@dfs.at');
INSERT INTO profile (birthdate,city,telnumber,education,photos,email)VALUES ('1995-01-24','Graz',06651444242,'Uni Wien', 3, 'aa@dfs.at');
INSERT INTO profile (birthdate,city,telnumber,education,photos,email)VALUES ('1995-01-25','Graz',06651444241,'Uni Wien', 5, 'aa@dfs.at');
INSERT INTO worker VALUES(3425623, 'Max', 'Gruber', '1980-07-11','http://vk.com', '2012-01-24');
INSERT INTO worker VALUES(4425623, 'Maria', 'Mueller', '1985-12-22','http://vk.com', '2012-01-25');
INSERT INTO developer VALUES(111111, 'M', 'a1232', 't53s35d',3425623);
INSERT INTO manager (managernr, emailM, telnumberM, pernr) VALUES(222222, 'bbb@ggg.at', 06762342253,4425623);


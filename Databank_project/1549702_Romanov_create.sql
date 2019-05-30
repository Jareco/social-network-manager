CREATE TABLE socialNetwork
(
    url VARCHAR(50),
    design VARCHAR(200),
    name VARCHAR(20) NOT NULL,
    CONSTRAINT pk_sn PRIMARY KEY(url)
);
CREATE TABLE user
(
    email VARCHAR(50),
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    url VARCHAR(20) NOT NULL,
    CONSTRAINT pk_user PRIMARY KEY(email),
    CONSTRAINT fk_user FOREIGN KEY(url) REFERENCES socialNetwork(url)
);
CREATE TABLE friendOf
(
    email1 VARCHAR(50),
    email2 VARCHAR(50),
    CONSTRAINT pk_frieandOf PRIMARY KEY(email1, email2),
    CONSTRAINT fk_frieandOf1 FOREIGN KEY(email1) REFERENCES user(email),
    CONSTRAINT fk_frieandOf2 FOREIGN KEY(email2) REFERENCES user(email)
);
CREATE TABLE profile
(
    id int NOT NULL AUTO_INCREMENT,
    birthdate DATE NOT NULL,
    city VARCHAR(50),
    telnumber BIGINT,
    education VARCHAR(50),
    photos INTEGER,
    email VARCHAR(50),
    CONSTRAINT pk_profil PRIMARY KEY (id,email),
    CONSTRAINT fk_profil FOREIGN KEY (email) REFERENCES user(email) ON DELETE CASCADE
);


CREATE TABLE worker
(
    pernr INTEGER(10) NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    birthdate DATE NOT NULL,
    url VARCHAR(50),
    CONSTRAINT pk_worker PRIMARY KEY(pernr),
    CONSTRAINT fk_worker FOREIGN KEY(url) REFERENCES socialNetwork(url)
);
CREATE TABLE developer
(
    developernr INTEGER(10) NOT NULL,
    nickname VARCHAR(50) NOT NULL,
    login VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    pernr INTEGER(10) NOT NULL,
    CONSTRAINT compare_developer CHECK (pernr != developernr),
    CONSTRAINT un_developer UNIQUE(nickname),
    CONSTRAINT pk_developer PRIMARY KEY(developernr),
    CONSTRAINT fk_developer FOREIGN KEY(pernr) REFERENCES worker(pernr) ON DELETE CASCADE
);
CREATE TABLE manager
(
    managernr INTEGER(10) NOT NULL,
    emailM VARCHAR(50) NOT NULL,
    telnumberM BIGINT NOT NULL,
    pernr INTEGER(10) NOT NULL,
    CONSTRAINT compare_manager CHECK (pernr != managernr),
    CONSTRAINT pk_manager PRIMARY KEY (managernr),
    CONSTRAINT fk_manager FOREIGN KEY (pernr) REFERENCES worker(pernr) ON DELETE CASCADE
);
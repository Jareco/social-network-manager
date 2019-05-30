/* Zahlt die Anzehl der Profile */
CREATE VIEW anzahl_user (Anzahl_Profile) AS
SELECT COUNT(id) 
FROM profil
;

/* Zeigt vorname,nachname und id, die den Benutzern gehoeren */
CREATE VIEW alle_user AS
  SELECT vorname,nachname,id
  FROM   benutzer INNER JOIN profil ON
  benutzer.email=profil.email
;
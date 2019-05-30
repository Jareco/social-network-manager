/* Zeigt, wie viele Profile (nach id) bei einer E-Mail angemelded sind */
CREATE VIEW anzahl_doppelt (Anzahl_id,E_Mail) AS
  SELECT COUNT(id), email
  FROM profil
  GROUP BY email
  HAVING COUNT(id) > 1 
;
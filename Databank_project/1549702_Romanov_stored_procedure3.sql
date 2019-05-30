create or replace PROCEDURE email_nachname(nn IN VARCHAR2, nachname OUT VARCHAR2) IS
BEGIN
  Select m.nachname INTO nachname from manager e,mitarbeiter m
where e.email_m=nn AND e.pernr=m.pernr;
END;
/
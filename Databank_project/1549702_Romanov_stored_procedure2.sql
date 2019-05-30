create or replace PROCEDURE name_nachname(nn IN VARCHAR2, nachname OUT VARCHAR2) IS
BEGIN
  Select m.nachname INTO nachname from entwickler e,mitarbeiter m
where e.nickname=nn AND e.pernr=m.pernr;
END;
/
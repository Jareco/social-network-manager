create or replace PROCEDURE name_nickname(nn IN VARCHAR2, nickname OUT VARCHAR2) IS
BEGIN
  Select e.nickname INTO nickname from entwickler e,mitarbeiter m
where m.nachname=nn AND e.pernr=m.pernr;
END;
/
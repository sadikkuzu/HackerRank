SELECT DISTINCT CITY
FROM STATION
where not regexp_like (CITY, '(a|e|i|o|u)$');
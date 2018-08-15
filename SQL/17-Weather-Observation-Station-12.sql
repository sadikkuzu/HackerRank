SELECT DISTINCT CITY
FROM STATION
where not regexp_like (CITY, '^(A|E|I|O|U)')
and not  regexp_like (CITY, '(a|e|i|o|u)$');
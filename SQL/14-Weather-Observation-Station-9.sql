SELECT DISTINCT CITY
FROM STATION
where not regexp_like (CITY, '^(A|E|I|O|U)');
SELECT DISTINCT CITY
FROM STATION
where  regexp_like (CITY, '^(A|E|I|O|U|a|e|i|o|u)');
SELECT DISTINCT(name) FROM people
WHERE name IS NOT 'Kevin Bacon' AND id IN (SELECT person_id FROM stars 
WHERE movie_id in
(select movie_id from stars where person_id in 
(select id from people where name = "Kevin Bacon"and birth = 1958)
));
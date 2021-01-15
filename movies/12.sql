SELECT title FROM movies
JOIN stars
ON movies.id = stars.movie_id
JOIN people
ON people.id = stars.person_id 
WHERE name  = "Helena Bonham Carter" and movie_id in
(select movie_id from stars where person_id in 
(select id from people where name = "Johnny Depp")
);
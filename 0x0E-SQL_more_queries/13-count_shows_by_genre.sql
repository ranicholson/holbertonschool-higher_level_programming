-- Scrit that shows all genres from the specified database and
-- displays number of shows linked to each
SELECT tg.name AS genre, COUNT(ts.genre_id)AS number_of_shows
FROM tv_genres AS tg
JOIN tv_show_genres AS ts
ON tg.id=ts.genre_id
GROUP BY ts.genre_id
ORDER BY number_of_shows DESC;

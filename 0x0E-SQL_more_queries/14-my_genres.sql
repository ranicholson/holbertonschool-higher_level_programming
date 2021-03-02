-- Script to list all genres of the show Dexter in the specified database
SELECT tg.name AS name
FROM tv_show_genres AS ts
JOIN tv_genres AS tg
ON ts.genre_id=tg.id
JOIN tv_shows AS t
ON t.id=ts.show_id
WHERE t.title = 'Dexter'
ORDER BY tg.name ASC;

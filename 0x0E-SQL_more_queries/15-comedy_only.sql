-- Script to list all comedy shows in specified database
SELECT ts.title
FROM tv_shows AS ts
JOIN tv_show_genres AS tg
ON ts.id=tg.show_id
JOIN tv_genres AS t
ON tg.genre_id=t.id
WHERE t.name="Comedy"
ORDER BY ts.title ASC;

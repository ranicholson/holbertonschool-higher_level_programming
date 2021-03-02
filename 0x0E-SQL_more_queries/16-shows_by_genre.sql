-- Script that lists all shows and genres linked to that show
SELECT ts.title, t.name
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tg
ON ts.id=tg.show_id
LEFT JOIN tv_genres AS t
ON tg.genre_id=t.id
ORDER BY ts.title ASC, t.name ASC;

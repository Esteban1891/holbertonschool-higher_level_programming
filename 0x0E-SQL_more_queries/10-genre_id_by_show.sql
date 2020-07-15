-- listing all shows contained in a db with at least one feature linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NOT NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

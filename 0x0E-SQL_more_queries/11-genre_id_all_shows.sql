-- list all shows contained in the db with at least one genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT OUTER JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
LEFT OUTER JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

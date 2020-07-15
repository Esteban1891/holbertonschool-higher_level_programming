-- listing all shows in db hbtn_0d_tvshows with no genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT OUTER JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
WHERE show_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

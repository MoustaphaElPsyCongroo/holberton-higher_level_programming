-- Lists all genres of the show Dexter
SELECT
	tv_genres.name
FROM
	tv_shows s
	INNER JOIN tv_show_genres g ON s.id = g.show_id
	INNER JOIN tv_genres ON g.genre_id = tv_genres.id
WHERE
	title = 'Dexter'
ORDER BY
	tv_genres.name

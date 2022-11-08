-- Counts the number of shows by genre
SELECT
	tv_genres.name,
	count(tv_genres.name) AS number_of_shows
FROM
	tv_genres
	LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY
	tv_genres.name
ORDER BY
	number_of_shows DESC

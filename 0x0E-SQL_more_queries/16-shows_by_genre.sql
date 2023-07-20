-- lists all show and genres linked to that show
SELECT title, name FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id LEFT JOIN tv_genres ON tv_show.genres_id = tv_genres.id ORDER BY title ASC, name ASC;

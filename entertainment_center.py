import media
import fresh_tomatoes


# My favorite movies
despicable_me = media.Movie("Despicable Me",
                            "Despicable masters and his Minions",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Despicable_Me_Poster.jpg/220px-Despicable_Me_Poster.jpg",
                            "https://www.youtube.com/watch?v=zzCZ1W_CUoI")

despicable_me_2 = media.Movie("Despicable Me 2",
                              "Second story of despicable masters and his Minions",
                              "https://upload.wikimedia.org/wikipedia/en/2/29/Despicable_Me_2_poster.jpg",
                              "https://www.youtube.com/watch?v=yM9sKpQOuEw")

despicable_me_3 = media.Movie("Despicable Me 3",
                              "Third story of despicable masters and his Minions",
                              "https://upload.wikimedia.org/wikipedia/en/9/91/Despicable_Me_3_%282017%29_Teaser_Poster.jpg",
                              "https://www.youtube.com/watch?v=6DBi41reeF0")

# List of movies
movies = [despicable_me, despicable_me_2, despicable_me_3]
fresh_tomatoes.open_movies_page(movies)

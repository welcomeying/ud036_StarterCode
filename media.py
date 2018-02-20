import webbrowser

class Movie():
	#class variables
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    #constructor
    def __init__(self, title, movie_storyline, poster_image, trailer_youtube):
    	self.title = title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #function for showing trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

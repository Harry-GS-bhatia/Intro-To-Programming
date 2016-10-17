class Movie():
    """...docstring..."""
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        """[docstring about the init , typically what the input argumnets do]"""
        """
        this function takes 1.movie title 2.story title 3.poster image 4.trailer youtube
        as input.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        """function that when called will help open the trailer"""
        webbrowser.open(self.trailer_youtube_url)
    
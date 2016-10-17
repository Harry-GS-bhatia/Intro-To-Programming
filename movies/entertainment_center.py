import fresh_tomatoes
import media 
import webbrowser
toy_story = media.Movie("toy story",
                        "it is the story of the boy whose toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc"
                        )
pursuit_of_happyness=media.Movie("pursuit of happyness",
                                 "Will Smith and his son, Jaden, bring to life the true story of a father-son family valiantly struggling to step up from the bottom rung of the ladder in 1980s San Francisco.", 
                                 "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                                 "https://youtu.be/89Kq8SDyvfg")


unbroken=media.Movie("unbroken",
                     "Louis Zamperini, a US Olympic track record holder, pulls himself through a plane crash in the Second World War only to be left at the mercy of nature and eventually caged up as a prisoner of war.",
                     "https://upload.wikimedia.org/wikipedia/en/7/76/Unbroken_poster.jpg",
                     "https://youtu.be/XrjJbl7kRrI")
a_beautiful_mind=media.Movie("a beautiful mind",
                             "John Nash, a brilliant but asocial mathematical genius, finds himself in pain when he encounters a cruel disorder. He ultimately overcomes his struggles and emerges free of any trauma.",
                             "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
                             "https://youtu.be/aS_d0Ayjw4o")

the_social_network=media.Movie("the social network",
                               "Mark Zuckerberg creates a social networking site, Facebook, with the help of his friend Eduardo Saverin. But soon, a string of lies tears their relationship apart even as Facebook connects people.",
                               "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                               "https://youtu.be/lB95KLmpLR4")
gladiator=media.Movie("gladiator",
                      "Commodus takes over power and demotes Maximus, one of the preferred generals of his father and predecessor, Emperor Marcus Aurelius. Maximus is relegated to fighting till death as a gladiator.",
                      "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                      "https://youtu.be/owK1qxDselE")


movies=[toy_story,pursuit_of_happyness,unbroken,a_beautiful_mind,the_social_network,gladiator]
fresh_tomatoes.open_movies_page(movies)
#print(media.movie.VALID_RATING)
#print(media.Movie.__doc__)
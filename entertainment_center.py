import media
import fresh_tomatoes

# This is the main program to run
# several movies are defined according to the Movie class
# and they are added to an array that is passed to
# the fresh_tomatoes.open_movies_page method
toy_story = media.Movie("Life is Beautiful",
                        "Italian comedian Roberto Benigni's World War II "
                        "era farce (released in the US both in Italian "
                        "with subtitles and dubbed into English) is a "
                        "tough proposition: Half the action is set in a"
                        "concentration camp, and its tragicomic inventions "
                        "are sometimes forced. The first half is standard "
                        "Benigni burlesque, complete with witty visual gags "
                        "and rapid-fire repartee",
                        "http://image.tmdb.org/t/p/original/f7DImXDebOs148U4uPjI61iDvaK.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=pAYEQP8gx3w")


guardian = media.Movie("Guardians of the Galaxy",
                       "A group of intergalactic criminals are forced to "
                       "work together to stop a fanatical warrior from "
                       "taking control of the universe.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=d96cjJhvlMA")


guardian2 = media.Movie("Guardians of the Galaxy II",
                        "The Guardians must fight to keep their newfound "
                        "family together as they unravel "
                        "the mystery of Peter Quill's true parentage.",
                        "https://i.annihil.us/u/prod/marvel/i/mg/9/c0/58d54d2cdc863/portrait_incredible.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=h7GiAwK2-fY")


green_mile = media.Movie("The Green Mile",
                         "The lives of guards on Death Row are affected "
                         "by one of their charges: a black man accused "
                         "of child murder and rape, yet who has a "
                         "mysterious gift.",
                         "https://images-na.ssl-images-amazon.com/images/I/412Z12RG9WL.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=Ki4haFrqSrw")


lion = media.Movie("Lion",
                   "A five-year-old Indian boy gets lost on the streets of "
                   "Calcutta, thousands of kilometers from home. He survives "
                   "many challenges before being adopted by a couple in "
                   "Australia. 25 years later, he sets out to find his lost "
                   "family.",
                   "http://fr.web.img2.acsta.net/r_1280_720/pictures/17/01/25/09/36/363964.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=ubKIgH8YWlA")

harry7 = media.Movie("Harry Potter 7",
                     "The film begins with Harry Potter (Daniel Radcliffe) "
                     "and Hermione Granger (Emma Watson) starting their "
                     "search for Voldemort's Horcruxes. Meanwhile, "
                     "Severus Snape arrives at Malfoy Manor to tell Voldemort "
                     "(Ralph Fiennes) and the rest of his council that he's "
                     "been appointed the new Headmaster of Hogwarts. He also "
                     "tells them that the Order of the Phoenix will be moving "
                     "Harry Potter from Privet Drive to a safe house. "
                     "Voldemort uses Lucius Malfoy's (Jason Isaacs) wand "
                     "to avoid using twin wands in a dueling battle.",
                     "http://vignette4.wikia.nocookie.net/harrypotter/images/a/ab/Deathly_Hallows_1_poster.jpg/revision/latest?cb=20151102033339",  # NOQA
                     "https://www.youtube.com/watch?v=_EC2tmFVNNE")

movies = [toy_story, guardian, guardian2, green_mile, lion, harry7]
fresh_tomatoes.open_movies_page(movies)

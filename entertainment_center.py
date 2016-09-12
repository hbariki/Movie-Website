import fresh_tomatoes
import media

# creating list of movies and intializing them with the constructor
toy_story = media.Movie("Toy Story",
                        "A story of the boy and his toys that come to life",
                        "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marien on an alien planet",
                     "http://imgs.abduzeedo.com/files/articles/Avatar/4154691413_a695e033a8_o.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

gladiator = media.Movie("Gladiator",
                        "A story of a warrior",
                        "http://www.movieposter.com/posters/archive/main/22/A70-11370",
                        "https://www.youtube.com/watch?v=ol67qo3WhJk")

titanic = media.Movie("Titanic",
                      "Titanic is a love story which takes place on the famous boat Titanic",
                      "http://media.hollywood.com/images/l/titanic-3d-poster.jpg",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

spider_man = media.Movie("Spider man",
                         "Spider man is a fictional superhero",
                         "http://vignette2.wikia.nocookie.net/spiderman-films/images/e/e7/Spider-Man_Poster.jpg/revision/latest?cb=20121104090100",
                         "https://www.youtube.com/watch?v=3R2uvJqWeVg")

bruce_almighty = media.Movie("Bruce Almighty",
                             "A guy who complains about god too often is given almighty powers",
                             "http://www.impawards.com/2003/posters/bruce_almighty.jpg",
                             "https://www.youtube.com/watch?v=fe-luzrqWSk")
# Adds the objects to movies
movies = [toy_story, avatar, gladiator, titanic, spider_man, bruce_almighty]
# calls the function open_movies_page from fresh tomatoes downloaded from udacity. Takes input as a list of movies and renders the data to a webpage
fresh_tomatoes.open_movies_page(movies)

# prints some pre-intializes class variables to the console.
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)

import fresh_tomatoes
import media

# create movie objects
there_will_be_blood = media.Movie('There Will Be Blood',
                     "The rise and fall of a turn of the century oil prospector",
                     'http://www.iceposter.com/thumbs/MOV_da486e79_b.jpg',
                     'https://youtu.be/OjZ1rUQQKxY')

apocalypse_now = media.Movie('Apocalypse Now',
                     'A army captain is sent to assassinate a renegade colonel',
                     'http://screencrush.com/files/2017/02/movie_poster.jpg',
                     'https://youtu.be/FTjG-Aux_yQ')

fargo = media.Movie('Fargo',
                     "A pregnant police officer pursues an inept criminal and his bungling henchmen",
                     'https://popculturerainman.files.wordpress.com/2014/02/936full-fargo-poster.jpg',
                     'https://youtu.be/h2tY82z3xXU')

# combine movie objects into a list
movies=[there_will_be_blood, fargo, apocalypse_now]

# pass movie object list to function to display movie page
fresh_tomatoes.open_movies_page(movies)

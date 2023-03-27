# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # movie : string, genre: string, rating: float
    
    # check if title, genre or rating are falsy
    if title == None or genre == None or rating == None:
        return None
    movie = {"title": title, "genre": genre, "rating": rating}
    
    return movie

def add_to_watched(user_data, movie):
    # user data is a dictionary with a key "watched"
        # the "watched" key's value is a list of dictioanries with each value being a movie the user has watched
        # empty list means no dictioanries in watched list
    
    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    # user_data us still a dictioanry
        # has key "watchlist" whos value is a list of movies the user wants to watch
    # add movie to watchlist (to be watched list)

    
    #user_data["watchlist"].append(movie)
    
    if user_data.get("watchlist") is None:
         user_data["watchlist"] = []

    user_data["watchlist"].append(movie)
    print(user_data["watchlist"])
    return user_data

def watch_movie(user_data, title):
    # user_data is dictionary
    # title is a string, title of movie user has watched

    # title is in user watchlist add movie to watched list, return user_data
    # if title is not in watchlist, return user_data

    print(title)
    index = 0
    for movie in user_data["watchlist"]:
        print(movie.get("title"))
        if movie.get("title") == title:
            print("in watch listtt")
            new_movie = create_movie(title, "", 0)
            add_to_watched(user_data, movie)

            #remove from watchlist
            #print(user_data["watchlist"])
            user_data["watchlist"].pop(index)
            
            #print(user_data["watchlist"])
        index += 1
    return user_data        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # calculate average of all ratings in watched list
    # empty watched returns 0.0
    # return average rating

    sum = 0.0
    if len(user_data["watched"]) == 0:
        return 0.0
    for movie in user_data["watched"]:
        sum += movie["rating"]
    
    return sum/len(user_data["watched"])

def get_most_watched_genre(user_data):
    # determine most frequently occuring genre

    if len(user_data["watched"]) == 0:
        return None
    genre_count = {}
    max = 0
    max_g = ""
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre_count.get(genre) == None:
            genre_count[genre] = 0
        else:
            genre_count[genre] += 1
            if genre_count[genre] > max:
                max = genre_count[genre]
                max_g = genre
    return max_g
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


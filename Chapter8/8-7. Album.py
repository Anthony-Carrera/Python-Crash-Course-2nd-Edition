"""
8-7. Album: Write a function called make_album() that builds a dictionary describing a music
album. The function should take in an artist name and an album title, and it should return a
dictionary containing these two pieces of information. Use the function to make three
dictionaries representing different albums. Print each return value to show that the dictionaries
are storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to store the number
of songs on an album. If the calling line includes a value for the number of songs, add that value
to the albums dictionary. Make at least one new function call that includes the number of songs
on an album.
"""
# This command ask the variable and artist name & ablum title
def make_album(artist_name,ablum_title, tracks=0):
    input = {'artist' : artist_name.title(),
             'ablum' : ablum_title.title()
             }
    if tracks:
        input['tracks'] = tracks
    return input

# This is the input the artist and user name, as well tracks
music = make_album('J cole','KOD')
print(music)
music = make_album('J cole','4 your eyes')
print(music)
music = make_album('J cole','Forest hill drive')
print(music)
music = make_album('J cole','Forest hill drive', tracks=8)
print(music)
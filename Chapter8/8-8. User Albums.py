"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows
users to enter an album is artist and title. Once you have that information, call make_album()
with the user is input and print the dictionary that is created. Be sure to include a quit value in the
while loop
"""
#This is the function for ablum, title and track 
def make_album(artist_name,ablum_title, tracks=0):
    input = {'artist' : artist_name.title(),
             'ablum' : ablum_title.title()
             }
    if tracks:
        input['tracks'] = tracks
    return input
#This is the while loop, q is to quit or 0 to quit if the track, it asked the user for artist,title and track. If it goes with trac, it does an other if statement to added it. If not it print out & artist,title

while True:
    print("Press q to quit.")
    art = input("\nName me an artists: ")
    if art == "q":
        break
    tit = input("\nName me an tilte: ")
    if tit == "q":
        break
    trac = input("Would you like added a track? Press y to continue: ")
    if trac == 'y':
        trac = input("\nWhat number me an track: ")
        trac = int(trac)
        together = make_album (art,tit,trac)
        print(together)
    else:
        together = make_album (art,tit)
        print(together)
    

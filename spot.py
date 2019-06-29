import sys
import spotipy
import pprint
import spotipy.util as util


scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)


if token:
    artists = []
    #sp = spotipy.Spotify(auth=token)
    #results = sp.search(q='Slayer', type='artist', limit=5)
    #items = results['artists']['items']
    #if len(items) > 0:
        #artist = items[0]
        #print(artist['name'], artist['images'][0]['url'])

    #pprint.pprint(results)
    #results = sp.current_user_saved_tracks()
    #for item in results['items']:
        #track = item['track']
        #print track['name'] + ' - ' + track['artists'][0]['name']

    # open the txt file containing the artist names pulled by 'scan'
    with open('ArtistList.txt', 'r') as work_data:
        for line in work_data:
            artists.append(line[:-1])
            
        # get spotify auth
        sp = spotipy.Spotify(auth=token)

        # for each artist, check if spotify search gets results
        for item in artists:
            results = sp.search(q=str(item), type='artist')
            items = results['artists']['items']
            if len(items) > 0:
                print("Artist found: " + str(item))


        
else:
    print "Can't get token for", username

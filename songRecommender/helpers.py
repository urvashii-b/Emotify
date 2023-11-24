import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="a1fad2fe15034d22a01403e112570344",
                                               client_secret="c194677d52d84c8d938953e086f30a2a",
                                               redirect_uri="http://localhost:8000",
                                               scope="user-read-playback-state streaming ugc-image-upload playlist-modify-public"),requests_timeout=10, retries=10)


def get_albums_id(ids):
    album_ids = []
    results = sp.artist_albums(ids)
    for album in results['items']:
        album_ids.append(album['id'])
    return album_ids

def get_album_songs_id(ids):
    song_ids = []
    results = sp.album_tracks(ids,offset=0)
    for songs in results['items']:
        song_ids.append(songs['id'])
    print(ids,song_ids)
    return song_ids

def get_songs_features(ids):

    meta = sp.track(ids)
    features = sp.audio_features(ids)

    # meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']
    ids =  meta['id']

    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    valence = features[0]['valence']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    key = features[0]['key']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, ids, release_date, popularity, length, danceability, acousticness,
            energy, instrumentalness, liveness, valence, loudness, speechiness, tempo, key, time_signature]
    columns = ['name','album','artist','id','release_date','popularity','length','danceability','acousticness','energy','instrumentalness',
                'liveness','valence','loudness','speechiness','tempo','key','time_signature']
    return track,columns

def get_songs_artist_ids_playlist(ids):
    playlist = sp.playlist_tracks(ids)
    songs_id = []
    artists_id = []
    for result in playlist['items']:
        songs_id.append(result['track']['id'])
        for artist in result['track']['artists']:
            artists_id.append(artist['id'])
    return songs_id,artists_id

def download_albums(music_id,artist=False):
    try:
        if artist == True:
            ids_album = get_albums_id(music_id)
        else:
            if type(music_id) == list:
                ids_album = music_id
            elif type(music_id) == str:
                ids_album = list([music_id])

        tracks = []
        for ids in ids_album:
            song_ids = get_album_songs_id(ids=ids)
            ids2 = song_ids
        
            print(f"Album Length: {len(song_ids)}")

            for song in ids2:
                track, columns = get_songs_features(song)
                tracks.append(track)

                print(f"Song Added: {track[0]} By {track[2]} from the album {track[1]}")
        print("Music Downloaded!")
        return tracks,columns
    except:
        return tracks,columns

def download_playlist(id_playlist,n_songs):
    try:
        songs_id = []
        tracks = []

        for i in range(0,n_songs,100):
            playlist = sp.playlist_tracks(id_playlist,limit=100,offset=i)

            for songs in playlist['items']:
                songs_id.append(songs['track']['id'])

        counter = 1
        for ids in songs_id:
        
            track,columns = get_songs_features(ids)
            tracks.append(track)

            print(f"Song {counter} Added:")
            print(f"{track[0]} By {track[2]} from the album {track[1]}")
            counter+=1
        print("Music Downloaded!")
        return tracks,columns
    except:
        return tracks,columns


from flask import Flask, jsonify, request
from ytmusicapi import YTMusic
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
ytmusic = YTMusic()
from flask import Flask, jsonify, request
from ytmusicapi import YTMusic

app = Flask(__name__)
ytmusic = YTMusic()


@app.route("/home")
def home():
    limit = int(request.args.get("limit", 3))
    search_results = ytmusic.get_home(limit=limit)
    return jsonify(search_results)

@app.route("/search")
def search():
    
    query = request.args.get("query")
    filter = request.args.get("filter")
    limit = int(request.args.get("limit", 20))
    search_results = ytmusic.search(query, filter=filter, limit=limit)
    return jsonify(search_results)

@app.route("/suggestions")
def suggestions():
     
    query = request.args.get("query")
    suggestions = ytmusic.get_search_suggestions(query=query)
    return jsonify(suggestions)

@app.route("/get_artist")
def get_artist():
   
    id = request.args.get("channelId")
    artist = ytmusic.get_artist(channelId=id)
    return jsonify(artist)

@app.route("/get_artist_releases")
def get_artist_releases():
    
    params = request.args.get("params")
    channelId = request.args.get("channelId")
    releases = ytmusic.get_artist_albums(channelId=channelId,params=params)
    return jsonify(releases)

@app.route("/get_user_info")
def get_user_info():
  
    channelId = request.args.get("channelId")
    user_info = ytmusic.get_user(channelId=channelId)
    return jsonify(user_info)

@app.route("/get_album")
def get_album():
   
    browseId = request.args.get("browseId")
    album = ytmusic.get_album(browseId=browseId)
    return jsonify(album)

@app.route("/get_song")
def get_song():
    video_id = request.args.get("videoId")
    song = ytmusic.get_song(videoId=video_id)
    return jsonify(song)

@app.route("/get_watch_playlists")
def get_watch_playlists():
    
    playlistId = request.args.get("playlistId",default=None)
    videoId = request.args.get("videoId",default=None)
    limit = int(request.args.get("limit",default=25))
    playlists = ytmusic.get_watch_playlist(playlistId=playlistId,videoId=videoId,limit=limit)
    return jsonify(playlists)

@app.route("/get_song_lyrics")
def get_song_lyrics():
    # browseId: Lyrics browse id obtained from get_watch_playlist
    lyricsId = request.args.get("lyricsId")
    lyrics = ytmusic.get_lyrics(browseId=lyricsId)
    return jsonify(lyrics)

@app.route("/get_mood_playlists")
def get_mood_playlists():
  
    mood_id = request.args.get("moodId")
    playlists = ytmusic.get_mood_playlists(params=mood_id)
    return jsonify(playlists)

@app.route("/get_basejs_url")
def get_genre_playlists():
    playlists = ytmusic.get_basejs_url()
    return jsonify(playlists)

@app.route("/get_country_charts")
def get_country_charts():
    country_code = request.args.get("countryCode",default='ZZ')
    charts = ytmusic.get_charts(country=country_code)
    return jsonify(charts)

@app.route("/get_playlist")
def get_playlist_contents():
    playlistId = request.args.get("playlistId")
    limit =int(request.args.get("limit",default=25))
    suggestionsLimit =int(request.args.get("suggestionsLimit",default=0))
    contents = ytmusic.get_playlist(playlistId=playlistId,limit=limit, related =True,   suggestions_limit= suggestionsLimit)
    return jsonify(contents)

@app.route("/get_library_playlists")
def get_playlist_suggestions():
   
    limit =int(request.args.get("limit",default=25))
    suggestions = ytmusic.get_library_playlists(limit=limit)
    return jsonify(suggestions)


if __name__ == "__main__":
    app.run()

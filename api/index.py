 
from flask import Flask, jsonify, render_template, request
from ytmusicapi import YTMusic
from flask_cors import CORS
import markdown 
from pytube import YouTube 

# ytmusic = YTMusic('oauth.json')

ytmusic = YTMusic()



app = Flask(__name__)
CORS(app) 



# app = Flask(__name__)
# CORS(app)
# cors = CORS(app, resource={
#     r"/*":{
#         "origins":"*"
#     }
# })

@app.route('/get_audio_urls', methods=['POST'])
def get_audio_urls():
    try:
        data = request.get_json()
        video_ids = data.get('video_ids', [])

        audio_urls = {}

        for video_id in video_ids:
            try:
                yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
                audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
                audio_url = audio_stream.url if audio_stream else None

                if audio_url:
                    audio_urls[video_id] = audio_url
                else:
                    audio_urls[video_id] = None
            except Exception as e:
                audio_urls[video_id] = None

        return jsonify(audio_urls), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# @app.route('/get_audio_url', methods=['GET'])
# def get_audio_url():
#     video_id = request.args.get('video_id')

#     if not video_id:
#         return jsonify({'error': 'Video ID parameter is missing'}), 400

#     try:
#         ydl_opts = {
#             'format': 'bestaudio/best',
#             'extractaudio': True,
#             'audioformat': 'mp3',
#             'outtmpl': 'downloads/%(id)s.%(ext)s',  # Download the audio file
#         }

#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             info_dict = ydl.extract_info(f'https://www.youtube.com/watch?v={video_id}', download=False)
#             audio_url = info_dict.get('url', '')

#         return jsonify({'audio_url': audio_url}), 200

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


@app.route("/")
def index():
    markdown_file_path = "./README.md"

    with open(markdown_file_path, "r", encoding="utf-8") as f:
        content = f.read()
        html_content = markdown.markdown(content)

    return render_template("index.html", content=html_content)


@app.route("/home")
def home():
    limit = int(request.args.get("limit", 12))
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
    releases = ytmusic.get_artist_albums(channelId=channelId, params=params)
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

    playlistId = request.args.get("playlistId", default=None)
    videoId = request.args.get("videoId", default=None)
    limit = int(request.args.get("limit", default=25))
    playlists = ytmusic.get_watch_playlist(
        playlistId=playlistId, videoId=videoId, limit=limit)
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
    country_code = request.args.get("countryCode", default='ZZ')
    charts = ytmusic.get_charts(country=country_code)
    return jsonify(charts)


@app.route("/get_playlist")
def get_playlist_contents():
    playlistId = request.args.get("playlistId")
    limit = int(request.args.get("limit", default=100))
    suggestionsLimit = int(request.args.get("suggestionsLimit", default=0))
    contents = ytmusic.get_playlist(
        playlistId=playlistId, limit=limit, related=True,   suggestions_limit=suggestionsLimit)
    return jsonify(contents)


@app.route("/get_library_playlists")
def get_playlist_suggestions():

    limit = int(request.args.get("limit", default=25))
    suggestions = ytmusic.get_library_playlists(limit=limit)
    return jsonify(suggestions)


@app.route("/get_mood_categories")
def get_mood_categories():
    data = ytmusic.get_mood_categories()
    return jsonify(data)


if __name__ == "__main__":
    app.run()

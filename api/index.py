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


@app.route("/search")
def search():
    """
    Search for songs, videos, albums, and playlists.

    Parameters:
    - `query` (str): The search query.
    - `filter` (str): Optional. The filter for the search results. Default is None.
    - `limit` (int): Optional. The maximum number of results to retrieve. Default is 20.

    Returns:
    - JSON object: The search results.
    """
    query = request.args.get("query")
    filter = request.args.get("filter")
    limit = int(request.args.get("limit", 20))
    search_results = ytmusic.search(query, filter=filter, limit=limit)
    return jsonify(search_results)

@app.route("/suggestions")
def suggestions():
    """
    Get search suggestions based on a query.

    Parameters:
    - `query` (str): The search query.

    Returns:
    - JSON object: The search suggestions.
    """
    query = request.args.get("query")
    suggestions = ytmusic.suggestions(query)
    return jsonify(suggestions)

@app.route("/get_artist")
def get_artist():
    """
    Get artist information.

    Parameters:
    - `artist_id` (str): The ID of the artist.

    Returns:
    - JSON object: The artist information.
    """
    artist_id = request.args.get("artist_id")
    artist = ytmusic.get_artist(artist_id)
    return jsonify(artist)

@app.route("/get_artist_releases")
def get_artist_releases():
    """
    Get releases (songs, videos, albums, singles) for an artist.

    Parameters:
    - `artist_id` (str): The ID of the artist.

    Returns:
    - JSON object: The artist releases.
    """
    artist_id = request.args.get("artist_id")
    releases = ytmusic.get_artist_albums(artist_id)
    return jsonify(releases)

@app.route("/get_user_info")
def get_user_info():
    """
    Get user information.

    Parameters:
    - `user_id` (str): The ID of the user.

    Returns:
    - JSON object: The user information.
    """
    user_id = request.args.get("user_id")
    user_info = ytmusic.get_user(user_id)
    return jsonify(user_info)

@app.route("/get_album")
def get_album():
    """
    Get album information.

    Parameters:
    - `album_id` (str): The ID of the album.

    Returns:
    - JSON object: The album information.
    """
    album_id = request.args.get("album_id")
    album = ytmusic.get_album(album_id)
    return jsonify(album)

@app.route("/get_song")
def get_song():
    """
    Get song metadata.

    Parameters:
    - `video_id` (str): The ID of the song video.

    Returns:
    - JSON object: The song metadata.
    """
    video_id = request.args.get("video_id")
    song = ytmusic.get_song(video_id)
    return jsonify(song)

@app.route("/get_watch_playlists")
def get_watch_playlists():
    """
    Get watch playlists (next songs when you press play/radio/shuffle).

    Parameters:
    - `video_id` (str): The ID of the video.

    Returns:
    - JSON object: The watch playlists.
    """
    video_id = request.args.get("video_id")
    playlists = ytmusic.get_watch_playlist(video_id)
    return jsonify(playlists)

@app.route("/get_song_lyrics")
def get_song_lyrics():
    """
    Get song lyrics.

    Parameters:
    - `video_id` (str): The ID of the song video.

    Returns:
    - JSON object: The song lyrics.
    """
    video_id = request.args.get("video_id")
    lyrics = ytmusic.get_lyrics(video_id)
    return jsonify(lyrics)

@app.route("/get_mood_playlists")
def get_mood_playlists():
    """
    Get playlists associated with a specific mood.

    Parameters:
    - `mood_id` (str): The ID of the mood.

    Returns:
    - JSON object: The mood playlists.
    """
    mood_id = request.args.get("mood_id")
    playlists = ytmusic.get_mood_playlists(mood_id)
    return jsonify(playlists)

@app.route("/get_genre_playlists")
def get_genre_playlists():
    """
    Get playlists associated with a specific genre.

    Parameters:
    - `genre_id` (str): The ID of the genre.

    Returns:
    - JSON object: The genre playlists.
    """
    genre_id = request.args.get("genre_id")
    playlists = ytmusic.get_genre_playlists(genre_id)
    return jsonify(playlists)

@app.route("/get_charts")
def get_charts():
    """
    Get the latest charts globally.

    Parameters:
    - `region_code` (str): Optional. The region code for the charts. Default is None.

    Returns:
    - JSON object: The global charts.
    """
    region_code = request.args.get("region_code")
    charts = ytmusic.get_charts(region_code=region_code)
    return jsonify(charts)

@app.route("/get_country_charts")
def get_country_charts():
    """
    Get the latest charts for a specific country.

    Parameters:
    - `country_code` (str): The two-letter country code.

    Returns:
    - JSON object: The country charts.
    """
    country_code = request.args.get("country_code")
    charts = ytmusic.get_charts(region_code=country_code)
    return jsonify(charts)

@app.route("/get_playlist_contents")
def get_playlist_contents():
    """
    Get the contents (songs, videos) of a playlist.

    Parameters:
    - `playlist_id` (str): The ID of the playlist.

    Returns:
    - JSON object: The playlist contents.
    """
    playlist_id = request.args.get("playlist_id")
    contents = ytmusic.get_playlist(playlist_id)
    return jsonify(contents)

@app.route("/get_playlist_suggestions")
def get_playlist_suggestions():
    """
    Get suggestions (recommended songs, videos) for a playlist.

    Parameters:
    - `playlist_id` (str): The ID of the playlist.

    Returns:
    - JSON object: The playlist suggestions.
    """
    playlist_id = request.args.get("playlist_id")
    suggestions = ytmusic.get_playlist_suggestions(playlist_id)
    return jsonify(suggestions)

if __name__ == "__main__":
    app.run()

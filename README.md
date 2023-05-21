## API Routes Documentation

This document provides an overview of the available routes and their usage for the API.

### Search

- **Endpoint:** `/search`
- **Method:** GET

#### Parameters

- `query` (str): The search query.
- `filter` (str, optional): The filter for the search results. Default is None.
- `limit` (int, optional): The maximum number of results to retrieve. Default is 20.

#### Returns

- JSON object: The search results.

### Suggestions

- **Endpoint:** `/suggestions`
- **Method:** GET

#### Parameters

- `query` (str): The search query.

#### Returns

- JSON object: The search suggestions.

### Get Artist

- **Endpoint:** `/get_artist`
- **Method:** GET

#### Parameters

- `artist_id` (str): The ID of the artist.

#### Returns

- JSON object: The artist information.

### Get Artist Releases

- **Endpoint:** `/get_artist_releases`
- **Method:** GET

#### Parameters

- `artist_id` (str): The ID of the artist.

#### Returns

- JSON object: The artist releases.

### Get User Info

- **Endpoint:** `/get_user_info`
- **Method:** GET

#### Parameters

- `user_id` (str): The ID of the user.

#### Returns

- JSON object: The user information.

### Get Album

- **Endpoint:** `/get_album`
- **Method:** GET

#### Parameters

- `album_id` (str): The ID of the album.

#### Returns

- JSON object: The album information.

### Get Song

- **Endpoint:** `/get_song`
- **Method:** GET

#### Parameters

- `video_id` (str): The ID of the song video.

#### Returns

- JSON object: The song metadata.

### Get Watch Playlists

- **Endpoint:** `/get_watch_playlists`
- **Method:** GET

#### Parameters

- `video_id` (str): The ID of the video.

#### Returns

- JSON object: The watch playlists.

### Get Song Lyrics

- **Endpoint:** `/get_song_lyrics`
- **Method:** GET

#### Parameters

- `video_id` (str): The ID of the song video.

#### Returns

- JSON object: The song lyrics.

### Get Mood Playlists

- **Endpoint:** `/get_mood_playlists`
- **Method:** GET

#### Parameters

- `mood_id` (str): The ID of the mood.

#### Returns

- JSON object: The mood playlists.

### Get Genre Playlists

- **Endpoint:** `/get_genre_playlists`
- **Method:** GET

#### Parameters

- `genre_id` (str): The ID of the genre.

#### Returns

- JSON object: The genre playlists.

### Get Charts

- **Endpoint:** `/get_charts`
- **Method:** GET

#### Parameters

- `region_code` (str, optional): The region code for the charts. Default is None.

#### Returns

- JSON object: The global charts.

### Get Country Charts

- **Endpoint:** `/get_country_charts`
- **Method:** GET

#### Parameters

- `country_code` (str): The two-letter country code.

#### Returns

- JSON object: The country charts.

### Get Playlist Contents

- **Endpoint:** `/get_playlist_contents`
- **Method:** GET

#### Parameters

- `playlist_id` (str): The ID of the playlist.

#### Returns

- JSON object: The playlist contents.

### Get Playlist Suggestions

- **Endpoint:** `/get_playlist_suggestions`
- **Method:** GET

#### Parameters

- `playlist_id` (str): The ID of the playlist.

#### Returns

- JSON object: The playlist suggestions.

Make sure to install the required packages (`flask` and `ytmusicapi`) and run the application using Python.

Remember to handle any potential errors or edge cases that may occur while making these requests, and customize the implementation as needed for your specific use case.

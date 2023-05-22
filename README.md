## API Routes Documentation

This document provides an overview of the available routes and their usage for the API.

### Endpoint
```javascript
https://python-music-server.vercel.app/
```

### Search

- **Endpoint:** `/search`
- **Method:** GET
```
    Search for songs, videos, albums, and playlists.

    Parameters:
    - `query` (str): The search query.
    - `filter` (str): Optional. The filter for the search results. Default is None.
    - `limit` (int): Optional. The maximum number of results to retrieve. Default is 20.

    Returns:
    - JSON object: The search results.
```

#### Parameters

- `query` (str): The search query.
- `filter` (str, optional): The filter for the search results. Default is None.
- `limit` (int, optional): The maximum number of results to retrieve. Default is 20.

#### Returns

- JSON object: The search results.

### Suggestions

- **Endpoint:** `/suggestions`
- **Method:** GET

    ```
    Get search suggestions based on a query.

    Parameters:
    - `query` (str): The search query.

    Returns:
    - JSON object: The search suggestions.
    ```

#### Parameters

- `query` (str): The search query.

#### Returns

- JSON object: The search suggestions.

### Get Artist

- **Endpoint:** `/get_artist`
- **Method:** GET

    ```
    Get artist information.

    Parameters:
    - `artist_id` (str): The ID of the artist.

    Returns:
    - JSON object: The artist information.
    ```

#### Parameters

- `artist_id` (str): The ID of the artist.

#### Returns

- JSON object: The artist information.

### Get Artist Releases

- **Endpoint:** `/get_artist_releases`
- **Method:** GET

```
    Get releases (songs, videos, albums, singles) for an artist.

    Parameters:
    - `artist_id` (str): The ID of the artist.

    Returns:
    - JSON object: The artist releases.
```

#### Parameters

- `artist_id` (str): The ID of the artist.

#### Returns

- JSON object: The artist releases.

### Get User Info

- **Endpoint:** `/get_user_info`
- **Method:** GET
```
    Get user information.

    Parameters:
    - `user_id` (str): The ID of the user.

    Returns:
    - JSON object: The user information.
```

#### Parameters

- `user_id` (str): The ID of the user.

#### Returns

- JSON object: The user information.

### Get Album

- **Endpoint:** `/get_album`
- **Method:** GET
```
    Get album information.

    Parameters:
    - `album_id` (str): The ID of the album.

    Returns:
    - JSON object: The album information.
```
#### Parameters

- `album_id` (str): The ID of the album.

#### Returns

- JSON object: The album information.

### Get Song

- **Endpoint:** `/get_song`
- **Method:** GET
```
    Get song metadata.

    Parameters:
    - `video_id` (str): The ID of the song video.

    Returns:
    - JSON object: The song metadata.
```
#### Parameters

- `video_id` (str): The ID of the song video.

#### Returns

- JSON object: The song metadata.

### Get Watch Playlists

- **Endpoint:** `/get_watch_playlists`
- **Method:** GET
```
    Get watch playlists (next songs when you press play/radio/shuffle).

    Parameters:
    - `video_id` (str): The ID of the video.

    Returns:
    - JSON object: The watch playlists.
```
#### Parameters

- `video_id` (str): The ID of the video.

#### Returns

- JSON object: The watch playlists.

### Get Song Lyrics

- **Endpoint:** `/get_song_lyrics`
- **Method:** GET
```
    Get song lyrics.

    Parameters:
    - `video_id` (str): The ID of the song video.

    Returns:
    - JSON object: The song lyrics.
```

#### Parameters

- `video_id` (str): The ID of the song video.

#### Returns

- JSON object: The song lyrics.

### Get Mood Playlists

- **Endpoint:** `/get_mood_playlists`
- **Method:** GET
```
    Get playlists associated with a specific mood.

    Parameters:
    - `mood_id` (str): The ID of the mood.

    Returns:
    - JSON object: The mood playlists.
```
#### Parameters

- `mood_id` (str): The ID of the mood.

#### Returns

- JSON object: The mood playlists.

### Get Genre Playlists

- **Endpoint:** `/get_genre_playlists`
- **Method:** GET
```
    Get playlists associated with a specific genre.

    Parameters:
    - `genre_id` (str): The ID of the genre.

    Returns:
    - JSON object: The genre playlists.
```
#### Parameters

- `genre_id` (str): The ID of the genre.

#### Returns

- JSON object: The genre playlists.

### Get Charts

- **Endpoint:** `/get_charts`
- **Method:** GET
```
Get the latest charts globally.

    Parameters:
    - `region_code` (str): Optional. The region code for the charts. Default is None.

    Returns:
    - JSON object: The global charts.
```
#### Parameters

- `region_code` (str, optional): The region code for the charts. Default is None.

#### Returns

- JSON object: The global charts.

### Get Country Charts

- **Endpoint:** `/get_country_charts`
- **Method:** GET
```
specific country.

    Parameters:
    - `country_code` (str): The two-letter country code.

    Returns:
    - JSON object: The country charts.
```
#### Parameters

- `country_code` (str): The two-letter country code.

#### Returns

- JSON object: The country charts.

### Get Playlist Contents

- **Endpoint:** `/get_playlist_contents`
- **Method:** GET
```
  Get the contents (songs, videos) of a playlist.

    Parameters:
    - `playlist_id` (str): The ID of the playlist.

    Returns:
    - JSON object: The playlist contents.
```
#### Parameters

- `playlist_id` (str): The ID of the playlist.

#### Returns

- JSON object: The playlist contents.

### Get Playlist Suggestions

- **Endpoint:** `/get_playlist_suggestions`
- **Method:** GET
```Get suggestions (recommended songs, videos) for a playlist.

    Parameters:
    - `playlist_id` (str): The ID of the playlist.

    Returns:
    - JSON object: The playlist suggestions.
```
#### Parameters

- `playlist_id` (str): The ID of the playlist.

#### Returns

- JSON object: The playlist suggestions.

Make sure to install the required packages (`flask` and `ytmusicapi`) and run the application using Python.

Remember to handle any potential errors or edge cases that may occur while making these requests, and customize the implementation as needed for your specific use case.

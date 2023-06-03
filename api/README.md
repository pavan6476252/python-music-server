## API Routes Documentation

This document provides an overview of the available routes and their usage for the API.

### Endpoint
```javascript
https://python-music-server.vercel.app/
```

## Home

**Endpoint:** `/home`

Retrieves home search results.

**Parameters:**
- `limit` (optional, int): The maximum number of results to retrieve. Default is 3.

**Returns:**
- JSON object: The search results.

---

## Search

**Endpoint:** `/search`

Searches for songs, videos, albums, and playlists.

**Parameters:**
- `query` (str): The search query.
- `filter` (optional, str): The filter for the search results. Default is None.
- `limit` (optional, int): The maximum number of results to retrieve. Default is 20.

**Returns:**
- JSON object: The search results.

---

## Suggestions

**Endpoint:** `/suggestions`

Gets search suggestions based on a query.

**Parameters:**
- `query` (str): The search query.

**Returns:**
- JSON object: The search suggestions.

---

## Get Artist

**Endpoint:** `/get_artist`

Retrieves artist information.

**Parameters:**
- `channelId` (str): The ID of the artist's channel.

**Returns:**
- JSON object: The artist information.

---

## Get Artist Releases

**Endpoint:** `/get_artist_releases`

Retrieves releases (songs, videos, albums, singles) for an artist.

**Parameters:**
- `channelId` (str): The ID of the artist's channel.
- `params` (optional, str): Additional parameters for filtering releases. Default is None.

**Returns:**
- JSON object: The artist releases.

---

## Get User Info

**Endpoint:** `/get_user_info`

Retrieves user information.

**Parameters:**
- `channelId` (str): The ID of the user's channel.

**Returns:**
- JSON object: The user information.

---

## Get Album

**Endpoint:** `/get_album`

Retrieves album information.

**Parameters:**
- `browseId` (str): The ID of the album.

**Returns:**
- JSON object: The album information.

---

## Get Song

**Endpoint:** `/get_song`

Retrieves song metadata.

**Parameters:**
- `videoId` (str): The ID of the song video.

**Returns:**
- JSON object: The song metadata.

---

## Get Watch Playlists

**Endpoint:** `/get_watch_playlists`

Retrieves watch playlists (next songs when you press play/radio/shuffle).

**Parameters:**
- `playlistId` (optional, str): The ID of the playlist. Default is None.
- `videoId` (optional, str): The ID of the video. Default is None.
- `limit` (optional, int): The maximum number of playlists to retrieve. Default is 25.

**Returns:**
- JSON object: The watch playlists.

---

## Get Song Lyrics

**Endpoint:** `/get_song_lyrics`

Retrieves song lyrics.

**Parameters:**
- `lyricsId` (str): The ID of the song's lyrics.

**Returns:**
- JSON object: The song lyrics.

---

## Get Mood Playlists

**Endpoint:** `/get_mood_playlists`

Retrieves playlists associated with a specific mood.

**Parameters:**
- `moodId` (str): The ID of the mood.

**Returns:**
- JSON object: The mood playlists.

---

---
## Get Moods 

**Endpoint:** `/get_mood_categories`

Retrieves get_mood_categories associated with a specific mood.

**Parameter

**Returns:**
- JSON object: Fetch “Moods & Genres” categories from YouTube Music.

---

## Get BaseJS URL

**Endpoint:** `/get_basejs_url`

Retrieves the BaseJS URL.

**Returns:**
- JSON object: The BaseJS URL.

---

## Get Country Charts

**Endpoint:** `/get_country_charts`

Retrieves the charts for a specific country.

**Parameters:**
- `countryCode` (optional, str): The country code. Default is 'ZZ' (global charts).

**Returns:**
- JSON object: The country charts.

---

## Get Playlist

**Endpoint:** `/get_playlist`

Retrieves the contents of a playlist.

**Parameters:**
- `playlistId` (str): The ID of the playlist.
- `limit` (optional, int): The maximum number of results to retrieve. Default is 25.
- `suggestionsLimit` (optional, int): The maximum number of suggested videos to retrieve. Default is 0.

**Returns:**
- JSON object: The playlist contents.

---

## Get Library Playlists

**Endpoint:** `/get_library_playlists`

Retrieves the playlists from the user's library.

**Parameters:**
- `limit` (optional, int): The maximum number of playlists to retrieve. Default is 25.

**Returns:**
- JSON object: The library playlists.

---

## Running the Application

The Flask application runs on the main thread using the `app.run()` method.


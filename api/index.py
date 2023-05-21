from flask import Flask, jsonify, request
from ytmusicapi import YTMusic
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
ytmusic = YTMusic()

@app.route('/search', methods=['GET'])
def search_songs():
    query = request.args.get('query')
    results = ytmusic.search(query, filter="songs")
    return jsonify(results)

@app.route('/home', methods=['GET'])
def get_home():
    home_content = ytmusic.get_home()
    return jsonify(home_content)

@app.route('/charts', methods=['GET'])
def get_home():
    query = request.args.get('query')
    home_content = ytmusic.get_charts(country=query)
    return jsonify(home_content)

@app.route('/playlist', methods=['GET'])
def get_home():
    query = request.args.get('query')
    home_content = ytmusic.get_playlist(playlistId=query)
    return jsonify(home_content)


if __name__ == '__main__':
    app.run()

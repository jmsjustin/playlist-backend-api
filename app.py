import db

from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"


@app.route("/songs.json")
def index():
    return db.songs_all()
@app.route("/songs.json", methods=["POST"])
def create():
    title = request.form.get("title")
    artist = request.form.get("artist")
    album = request.form.get("album")
    url = request.form.get("url")
    return db.songs_create(title,artist,album,url)

@app.route("/songs/<id>.json", methods=["PATCH"])
def update(id):
    title = request.form.get("title")
    artist = request.form.get("artist")
    album = request.form.get("album")
    url = request.form.get("url")
    return db.songs_update_by_id(id, title, artist, album, url)

@app.route("/songs/<id>.json")
def show(id):
    return db.songs_find_by_id(id)

@app.route("/songs/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.songs_destroy_by_id(id)

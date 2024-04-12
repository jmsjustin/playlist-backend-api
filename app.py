import db

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

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

@app.route("/songs/<id>.json")
def show(id)
return db.songs_find_by_id(id)

@pp.route("/songs/<id>.json", methods=[DELETED])
def destroy(id):
    return db.songs_destroy_by_id(id)
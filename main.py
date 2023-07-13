import spotipy
import youtube_dl
import yt_dlp as youtube_dl
from spotipy.oauth2 import SpotifyClientCredentials
from youtubesearchpython import VideosSearch
import json
import os
from datetime import datetime
import configparser
config_object = configparser.ConfigParser()


def firstlaunch():
    client_id = str(input("Enter Spotify Client ID to save on Confiuration File: "))
    client_secret = str(input("Enter Spotify Client ID to save on Confiuration File: "))
    config_object.add_section("spotify")
    config_object.set("spotify","client_id",f"{client_id}")
    config_object.set("spotify","client_secret",f"{client_secret}")
    with open("configuration.ini","w") as file_object:
        config_object.write(file_object)


def startup():
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H-%M-%S")
    
    if not os.path.exists("log"):
        os.makedirs('log')
    return timestamp


def youtubeSearch(trackname:str, artistname:str):
    videosSearch = VideosSearch(f"{trackname}-{artistname}", limit = 1)
    ytsearch_ = json.loads(json.dumps(videosSearch.result()))

    link = ytsearch_['result'][0]['link']
    title = ytsearch_['result'][0]['title']
    return link, title

def youtubeDownload(link, title):
    if not os.path.exists('music'):
        os.makedirs('music')
    video_info = youtube_dl.YoutubeDL().extract_info(url = link,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':f"music/{filename}",
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Download complete... {}".format(filename))
    return filename,link, title

def completedFiles(filename, link, title):
    log = open(f"log/{timestamp}.txt", "w")
    log.write(f"/n {filename} /t {link} /t {title}")
    log.close()
    
if not os.path.exists("configuration.ini"):
    firstlaunch()

with open("configuration.ini","r") as file_object:
    config_object.read_file(file_object)
    client_id_str =config_object.get("spotify","client_id")
    client_secret_str =config_object.get("spotify","client_secret")

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=client_id_str, client_secret=client_secret_str)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_link = str(input("link: "))

playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

timestamp = startup()


for track in sp.playlist_tracks(playlist_URI)["items"]: 
    track_name = track["track"]["name"]
    artist_name = track["track"]["artists"][0]["name"]
    music = track_name+"-"+artist_name
    music_list = list()
    link, title = youtubeSearch(track_name, artist_name)
    filename, link, title = youtubeDownload(link, title)
    completedFiles(filename, link, title)






import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path= ".env")

API_KEY = "AIzaSyBfUmQTDLbrmUxlL9-6mHa5fXkpL866pvI"
CHANNEL_HANDLE = "MrBeast"

def get_playlist_id():

    try:

        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response =  requests.get(url)

        data = response.json()

        #print(json.dumps(data,indent=4))

        channel_items = data["items"][0]
        
        channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        print(channel_playlistId)
        
        return channel_playlistId
    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    get_playlist_id()

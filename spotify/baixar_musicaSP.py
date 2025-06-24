import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import yt_dlp
import re

def get_spotify_playlist_tracks(playlist_url):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id="Seu client id",
        client_secret="Seu client secret"
    ))

    playlist_id = playlist_url.split('/')[-1].split('?')[0]

    results = sp.playlist_tracks(playlist_id)
    track = results['items']

    # Paginar até pegar tudo
    while results['next']:
        results = sp.next(results)
        track.extend(results['items'])
    tracks = []

    for item in track:
        track_name = item['track']['name']
        artist_name = item['track']['artists'][0]['name']
        tracks.append(f"{track_name} {artist_name}")

    return tracks


def download_track(track_name):
    track_name = re.sub(r'[\\/:*?"<>|]', '_', track_name)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'./downloads/{track_name}.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ],
        'quiet': False,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch:{track_name}"])


def main(playlist_url):
    tracks = get_spotify_playlist_tracks(playlist_url)
    print(f"Encontradas {len(tracks)} músicas na playlist.")

    # Criar diretório para armazenar as músicas
    import os
    if not os.path.exists('./musicas_spotify'):
        os.makedirs('./musicas_spotify')

    for track in tracks:
        print(f"Baixando: {track}")
        download_track(track)


# URL da playlist do Spotify
playlist_url = "URL da sua playlist"

main(playlist_url)
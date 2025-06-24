import yt_dlp
import os

def baixar_audios_playlist(playlist_url, pasta_destino):
    # Cria a pasta de destino se não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Configurações para baixar apenas o áudio com yt_dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    # Baixa a playlist
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
    print("Download concluído.")

# Exemplo de uso
playlist_url = input("Insira o link da playlist do YouTube: ")
pasta_destino = "Musicas python"
baixar_audios_playlist(playlist_url, pasta_destino)
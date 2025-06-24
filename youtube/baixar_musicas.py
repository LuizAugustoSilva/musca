from pytube import Playlist, YouTube
from pydub import AudioSegment
import os

def baixar_audios_playlist(playlist_url, pasta_destino):
    # Cria a pasta de destino se não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Acessa a playlist no YouTube
    playlist = Playlist(playlist_url)
    print(f"Baixando áudios de {len(playlist.video_urls)} vídeos...")

    # Percorre todos os vídeos na playlist
    for video_url in playlist.video_urls:
        try:
            # Obtém o objeto de vídeo e baixa o áudio
            yt = YouTube(video_url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_file_path = audio_stream.download(output_path=pasta_destino)
            
            # Converte para MP3
            audio_mp3_path = os.path.splitext(audio_file_path)[0] + ".mp3"
            audio = AudioSegment.from_file(audio_file_path)
            audio.export(audio_mp3_path, format="mp3")
            
            # Remove o arquivo original (.webm ou .mp4)
            os.remove(audio_file_path)
            
            print(f"Baixado e convertido: {yt.title}")
        except Exception as e:
            print(f"Erro ao baixar {video_url}: {e}")

# Exemplo de uso
playlist_url = input("Insira o link da playlist do YouTube: ")
pasta_destino = "Musicas python"
baixar_audios_playlist(playlist_url, pasta_destino)
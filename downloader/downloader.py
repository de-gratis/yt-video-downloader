import os
from pytube import YouTube, Playlist
from pytube.cli import on_progress


def baixar_yt_video(link:str, mp3:bool=False) -> None:
    while True:
        if link == 'n':
            break
        else:
            try:
                yt = YouTube(link, on_progress_callback=on_progress)

                print(f'O título deste vídeo é: {yt.title}')

                if mp3:
                    out_file = yt.streams.filter(only_audio=True).first().download(output_path='downloads')
                    base = os.path.splitext(out_file)[0]
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                else:
                    yt.streams.get_highest_resolution().download(output_path='downloads')
                print('Download concluído com sucesso')
                break
            except Exception as error:
                print('ERRO: ', error)
                continue


def baixar_yt_playlist(link:str, mp3:bool) -> None:
    playlist = Playlist(link)
    print(f'Número de vídeo na playlist: {len(playlist.video_urls)}')

    for video_url in playlist.video_urls:
        baixar_yt_video(video_url, mp3)

from pytube import YouTube, Playlist
from pytube.cli import on_progress


def baixar_yt_video(link):
    while True:
        if link == 'n':
            break
        else:
            try:
                yt = YouTube(link,on_progress_callback=on_progress)

                print(f'O título deste vídeo é: {yt.title}')
            except Exception as error:
                print('ERRO: ', error)
                continue

            try:
                yt.streams.get_highest_resolution().download()
                print('Download concluído com sucesso')
                break
            except Exception as error:
                print('ERRO: ', error)


def baixar_yt_playlist(link):
    playlist = Playlist(link)
    print(f'Número de vídeo na playlist: {len(playlist.video_urls)}')

    for video_url in playlist.video_urls:
        baixar_yt_video(video_url)

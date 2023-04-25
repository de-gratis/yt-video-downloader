from pytube import YouTube, Playlist


def baixar_yt_video(link):
    while True:
        if link == 'n':
            break
        else:
            try:
                yt = YouTube(link)

                print(f'O título deste vídeo é: {yt.title}')
            except:
                print('Erro em alguma coisa')
                continue

            try:
                yt.streams.get_highest_resolution().download()
                print('Download concluído com sucesso')
                break
            except:
                print('Erro ao fazer download do arquivo')


def baixar_yt_playlist(link):
    playlist = Playlist(link)
    print(f'Número de vídeo na playlist: {len(playlist.video_urls)}')

    for video_url in playlist.video_urls:
        baixar_yt_video(video_url)

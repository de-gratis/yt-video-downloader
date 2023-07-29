from downloader import baixar_yt_video, baixar_yt_playlist

menu = '''
### Em .mp4
[1] Baixar vídeo
[2] Baixar playlist
### Em .mp3
[3] Baixar vídeo
[4] Baixar playlist
Digite sua opção: '''

if __name__ == '__main__':
    while True:
        match input(menu):
            case '1':
                baixar_yt_video(input('Digite o link do seu vídeo: '))
            case '2':
                baixar_yt_playlist(input('Digite o link da sua playlist: '))
            case '3':
                baixar_yt_video(input('Digite o link do seu vídeo: '), True)
            case '4':
                baixar_yt_playlist(input('Digite o link da sua playlist: '), True)
            case _:
                break

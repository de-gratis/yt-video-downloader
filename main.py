from downloader import baixar_yt_video, baixar_yt_playlist

menu = '''
[1] Baixe um vídeo do YouTube colando seu link
[2] Baixe uma playlist do YouTube colando seu link
Digite sua opção: '''

if __name__ == '__main__':
    while True:
        escolha = input(menu)
        if escolha == '1':
            baixar_yt_video(input('Digite o link do seu vídeo: '))
        elif escolha == '2':
            baixar_yt_playlist(input('Digite o link da sua playlist: '))
        else:
            break

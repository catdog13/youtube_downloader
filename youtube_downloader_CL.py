import youtube_dl


def main_loop():
    # test link http://www.youtube.com/watch?v=BaW_jenozKc
    def options():
        audio = False
        if audio is True:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '256',
                }],
            }
        else:
            ydl_opts = {}
        return ydl_opts

    def downloader(link, opts):
        with youtube_dl.YoutubeDL(opts) as ydl:
            ydl.download([link])

    input_link = input('Enter link here: ')
    downloader(input_link, options())


if __name__ == '__main__':
    while True:
        main_loop()

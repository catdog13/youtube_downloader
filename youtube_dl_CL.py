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

    link_file = open('urls.txt')
    for line in link_file:
        downloader(line, options())
        print("Done")

if __name__ == '__main__':
    main_loop()

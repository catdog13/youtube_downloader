from tkinter import Tk, Label, Entry, Button, IntVar, Checkbutton, END
import youtube_dl


class MainWindow:
    def __init__(self, window):
        self.window = window
        window.title("youtube-dl GUI")
        Label(window, text="URL# 1").grid(row=1, column=1)
        Label(window, text="URL# 2").grid(row=2, column=1)
        Label(window, text="URL# 3").grid(row=3, column=1)
        Label(window, text="URL# 4").grid(row=4, column=1)
        Label(window, text="URL# 5").grid(row=5, column=1)
        self.url1 = Entry(window, width=50)
        self.url2 = Entry(window, width=50)
        self.url3 = Entry(window, width=50)
        self.url4 = Entry(window, width=50)
        self.url5 = Entry(window, width=50)
        self.url1.grid(row=1, column=2, padx=5, pady=10)
        self.url2.grid(row=2, column=2, padx=5, pady=10)
        self.url3.grid(row=3, column=2, padx=5, pady=10)
        self.url4.grid(row=4, column=2, padx=5, pady=10)
        self.url5.grid(row=5, column=2, padx=5, pady=10)
        Button(window, text="Done", command=window.quit).grid(row=7, column=1, pady=10)
        self.checked1 = IntVar()
        self.checked2 = IntVar()
        self.checked3 = IntVar()
        self.checked4 = IntVar()
        self.checked5 = IntVar()
        Checkbutton(window, text="Audio Only", variable=self.checked1).grid(row=1, column=3)
        Checkbutton(window, text="Audio Only", variable=self.checked2).grid(row=2, column=3)
        Checkbutton(window, text="Audio Only", variable=self.checked3).grid(row=3, column=3)
        Checkbutton(window, text="Audio Only", variable=self.checked4).grid(row=4, column=3)
        Checkbutton(window, text="Audio Only", variable=self.checked5).grid(row=5, column=3)
        Button(window, text="Download", command=self.download).grid(row=7, column=3, pady=10)
        Button(window, text="Clear", command=self.clear_inputs).grid(row=7, column=2)

    def download(self):  # test link http://www.youtube.com/watch?v=BaW_jenozKc
        def downloader(link, opts):
            with youtube_dl.YoutubeDL(opts) as ydl:
                ydl.download([link])

        def downloader_opts(audio_check):
            if audio_check != 0:  # 6
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
        link1 = self.url1.get()
        link2 = self.url2.get()
        link3 = self.url3.get()
        link4 = self.url4.get()
        link5 = self.url5.get()
        if link1 != "":
            audio1 = self.checked1.get()
            downloader(link1, downloader_opts(audio1))
            print("Done")
        else:
            print("URL# 1 is empty")
        if link2 != "":
            audio2 = self.checked2.get()
            downloader(link2, downloader_opts(audio2))
            print("Done")
        else:
            print("URL# 2 is empty")
        if link3 != "":
            audio3 = self.checked3.get()
            downloader(link3, downloader_opts(audio3))
            print("Done")
        else:
            print("URL# 3 is empty")
        if link4 != "":
            audio4 = self.checked4.get()
            downloader(link4, downloader_opts(audio4))
            print("Done")
        else:
            print("URL# 4 is empty")
        if link5 != "":
            audio5 = self.checked5.get()
            downloader(link5, downloader_opts(audio5))
            print("Done")
        else:
            print("URL# 5 is empty")
        print("Done")

    def clear_inputs(self):  # clearing the entry boxes
        self.url1.delete(0, END)  # deleting from first to the end
        self.url2.delete(0, END)
        self.url3.delete(0, END)
        self.url4.delete(0, END)
        self.url5.delete(0, END)
        self.checked1.set(0)
        self.checked2.set(0)
        self.checked3.set(0)
        self.checked4.set(0)
        self.checked5.set(0)

if __name__ == '__main__':
    root = Tk()
    my_gui = MainWindow(root)
    root.mainloop()

import tkinter as tk
import youtube_dl


class App:
    def __init__(self):
        def gui():
            global url1, url2, url3, url4, url5, checked1, checked2, checked3, checked4, checked5
            root.title("youtube-dl GUI")
            tk.Label(root, text="URL# 1").grid(row=1, column=1)
            tk.Label(root, text="URL# 2").grid(row=2, column=1)
            tk.Label(root, text="URL# 3").grid(row=3, column=1)
            tk.Label(root, text="URL# 4").grid(row=4, column=1)
            tk.Label(root, text="URL# 5").grid(row=5, column=1)
            url1 = tk.Entry(root, width=50)
            url2 = tk.Entry(root, width=50)
            url3 = tk.Entry(root, width=50)
            url4 = tk.Entry(root, width=50)
            url5 = tk.Entry(root, width=50)
            url1.grid(row=1, column=2, padx=5, pady=10)
            url2.grid(row=2, column=2, padx=5, pady=10)
            url3.grid(row=3, column=2, padx=5, pady=10)
            url4.grid(row=4, column=2, padx=5, pady=10)
            url5.grid(row=5, column=2, padx=5, pady=10)
            tk.Button(root, text="Done", command=root.quit).grid(row=7, column=1, pady=10)
            checked1 = tk.IntVar()
            checked2 = tk.IntVar()
            checked3 = tk.IntVar()
            checked4 = tk.IntVar()
            checked5 = tk.IntVar()
            tk.Checkbutton(root, text="Audio Only", variable=checked1).grid(row=1, column=3)
            tk.Checkbutton(root, text="Audio Only", variable=checked2).grid(row=2, column=3)
            tk.Checkbutton(root, text="Audio Only", variable=checked3).grid(row=3, column=3)
            tk.Checkbutton(root, text="Audio Only", variable=checked4).grid(row=4, column=3)
            tk.Checkbutton(root, text="Audio Only", variable=checked5).grid(row=5, column=3)
            return url1, url2, url3, url4, url5, checked1, checked2, checked3, checked4, checked5
        gui()

        def download():  # test link http://www.youtube.com/watch?v=BaW_jenozKc
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
            link1 = url1.get()
            link2 = url2.get()
            link3 = url3.get()
            link4 = url4.get()
            link5 = url5.get()
            if link1 != "":
                audio1 = checked1.get()
                downloader(link1, downloader_opts(audio1))
                print("Done")
            else:
                print("URL# 1 is empty")
            if link2 != "":
                audio2 = checked2.get()
                downloader(link2, downloader_opts(audio2))
                print("Done")
            else:
                print("URL# 2 is empty")
            if link3 != "":
                audio3 = checked3.get()
                downloader(link3, downloader_opts(audio3))
                print("Done")
            else:
                print("URL# 3 is empty")
            if link4 != "":
                audio4 = checked4.get()
                downloader(link4, downloader_opts(audio4))
                print("Done")
            else:
                print("URL# 4 is empty")
            if link5 != "":
                audio5 = checked5.get()
                downloader(link5, downloader_opts(audio5))
                print("Done")
            else:
                print("URL# 5 is empty")
            print("Done")
        tk.Button(root, text="Download", command=download).grid(row=7, column=3, pady=10)

        def clear_inputs():  # clearing the entry boxes
            url1.delete(0, tk.END)  # deleting from first to the end
            url2.delete(0, tk.END)
            url3.delete(0, tk.END)
            url4.delete(0, tk.END)
            url5.delete(0, tk.END)
            checked1.set(0)
            checked2.set(0)
            checked3.set(0)
            checked4.set(0)
            checked5.set(0)
        tk.Button(root, text="Clear", command=clear_inputs).grid(row=7, column=2)  # button to start the clearing

root = tk.Tk()
app = App()
root.mainloop()

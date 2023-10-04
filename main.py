import tkinter
import customtkinter
from pytube import YouTube
from pytube import exceptions

def start_download():
    try:
        youtube_link = link.get()
        youtube_object = YouTube(youtube_link, on_progress_callback=on_progress)
        video = youtube_object.streams.get_highest_resolution()
        title.configure(text=youtube_object.title, text_color="green")
        finish_label.configure(text="")
        video.download("")
        finish_label.configure(text="Downloaded!", text_color="green")
    except exceptions.RegexMatchError:
        finish_label.configure(text="Invalid Link!", text_color="red")


def on_progress(stream, chunk, bytes_remain):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remain
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pb_percentage.configure(text=f"% {per}")
    pb_percentage.update()
    progress_bar.set(float(percentage_of_completion) / 100)  # between 0 and 1


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert a Youtube video link: ")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=360, height=28, textvariable=url_var)
link.pack(padx=10, pady=15)

download_button = customtkinter.CTkButton(app, text="Download", command=start_download)
download_button.pack(padx=10, pady=20)

finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

pb_percentage = customtkinter.CTkLabel(app, text="0")
pb_percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=360)
progress_bar.pack(padx=10, pady=30)
progress_bar.set(0)

app.mainloop()

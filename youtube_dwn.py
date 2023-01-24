from tkinter import messagebox
from pytube import YouTube
from tkinter import *


def dwn():
    """Takes a url and downloads the corresponding youtube video"""
    link = str(ent.get())
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.download('/Users/jack/Movies')
    messagebox.showinfo("Success", "Video downloaded successfully")


win = Tk()
win.title("YouTube Downloader")
win.geometry("640x100")

text = Label(win, text = "YouTube video link:")
ent = Entry(win, width = 600)
btn = Button(win, text="Download", command=dwn)
ent.pack()
btn.pack()
win.mainloop()

from tkinter import messagebox
from pytube import YouTube
from tkinter import *
from tkinter import filedialog as tkFileDialog

def dwn():
    """Takes a url and downloads the corresponding youtube video"""
    directory = tkFileDialog.askdirectory()
    link = str(ent.get())
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.download(directory)
    messagebox.showinfo("Success", "Video downloaded successfully")


win = Tk()
# uncomment as needed
# win.iconbitmap(default="path_to_ico_file")
win.title("YouTube Downloader")
win.geometry("640x100")

text = Label(win, text = "YouTube video link:")
ent = Entry(win, width = 600)
btn = Button(win, text="Download", command=dwn)
ent.pack()
btn.pack()
win.mainloop()

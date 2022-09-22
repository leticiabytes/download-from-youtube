import pytube
from pytube import *

import tkinter as tk
from tkinter import filedialog

url = input('Enter video url: ')

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()

myVideo = pytube.YouTube(url).streams.get_highest_resolution().download(file_path)
print(myVideo.title)
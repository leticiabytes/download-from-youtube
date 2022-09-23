import pytube
from pytube import *
from pytube.cli import on_progress

from plyer import notification

import tkinter as tk
from tkinter import filedialog

url = input('Enter video url: ')

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()

video = pytube.YouTube(url).streams.get_highest_resolution()
video.download(file_path)

notification.notify(
  title = "Download concluído",
  message = str(video.title) + " foi baixado",
  timeout = pytube.YouTube(url, on_progress_callback=on_progress)
)
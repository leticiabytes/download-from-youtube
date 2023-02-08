import tkinter as tk
from tkinter import filedialog
import requests
import shutil
import os
from pytube import YouTube
from tqdm import tqdm

def download_video():
    # Get the video URL from the user
    video_url = url_entry.get()
    # Get the directory to save the video from the user
    download_path = filedialog.askdirectory()
    # Create the YouTube object
    yt = YouTube(video_url)
    # Get the video from YouTube
    video = yt.streams.first()
    # Create the progress bar
    pbar = tqdm(total=video.filesize)
    # Define the progress callback function
    def progress_function(chunk, file_handle, bytes_remaining):
        # Update the progress bar
        pbar.update(video.filesize - bytes_remaining)
    # Download the video
    video.download(download_path, on_progress=progress_function)
    # Close the progress bar
    pbar.close()

# Create the GUI
root = tk.Tk()
root.title('YouTube Downloader')
root.geometry('400x100')

# Add a label
label = tk.Label(root, text='Enter the YouTube video URL')
label.grid(row=0, column=0, padx=10, pady=10)

# Add a text entry box
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Add a download button
download_button = tk.Button(root, text='Download Video', command=download_video)
download_button.grid(row=1, column=1, padx=10, pady=10)

# Run the GUI
root.mainloop()

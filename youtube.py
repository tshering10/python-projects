from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download(url, path):
    try:
        yt = YouTube(url)
        
        # Filter streams for mp4 files with progressive download (audio + video)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        
        # Get the stream with the highest resolution
        stream = streams.get_highest_resolution()
        
        # Download the video
        stream.download(output_path=path)
        
        print("Video Downloaded Successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Sample YouTube URL and download path
url = "https://www.youtube.com/watch?v=NpmFbWO6HPU&t=25202s&ab_channel=TechWithTim"
path = "C:/Users/LENEVO/Desktop/tsheringtamang"  # Make sure this folder exists
download(url, path)

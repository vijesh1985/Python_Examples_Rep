import pytube
from pytube import YouTube
from pytube.cli import on_progress
import logging, requests
from datetime import datetime

def downloader(link):
    start_time = datetime.now()
    print(f"Start time : {start_time} \t")
    #check_link = check_availability(link)
    #print(f"Checking Link.. : {check_link}")
    try:
        youtubeObject = YouTube(link, on_progress_callback=on_progress)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download('C:/Users/vijes/Downloads')
    except Exception as e:
        logging.error('Failed to download: '+ str(e))
        return
    end_time = datetime.now()
    time_diff = end_time - start_time
    print(f"End time : {end_time} \t")
    print("Download Completed in - {} \t".format(time_diff))

link = input("Put the YouTube link here (URL) : ")
downloader(link)

import tkinter as tk
from tkinter import filedialog
import urllib.request
import praw
import os


def start_download():
    subreddit_name = subreddit_entry.get()
    upvote_threshold = int(threshold_entry.get())
    download_folder = folder_entry.get()
    download_images(subreddit_name, upvote_threshold, download_folder)


def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)


def download_images(subreddit_name, upvote_threshold, download_folder):
    reddit = praw.Reddit(
        client_id="",
        client_secret="",
        password="",
        user_agent="",
        username="",
    )
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.hot(limit=100):
        if submission.score > upvote_threshold and (submission.url.endswith('.jpg') or submission.url.endswith('.png')):
            image_path = os.path.join(download_folder, f"{submission.id}.jpg")
            urllib.request.urlretrieve(submission.url, image_path)


root = tk.Tk()
root.title("Image Downloader")

subreddit_label = tk.Label(root, text="Subreddit:")
subreddit_label.grid(row=0, column=0)
subreddit_entry = tk.Entry(root)
subreddit_entry.grid(row=0, column=1)

threshold_label = tk.Label(root, text="Upvote threshold:")
threshold_label.grid(row=1, column=0)
threshold_entry = tk.Entry(root)
threshold_entry.grid(row=1, column=1)

folder_label = tk.Label(root, text="Download folder:")
folder_label.grid(row=2, column=0)
folder_entry = tk.Entry(root)
folder_entry.grid(row=2, column=1)
folder_button = tk.Button(root, text="Browse", command=browse_folder)
folder_button.grid(row=2, column=2)

download_button = tk.Button(root, text="Download", command=start_download)
download_button.grid(row=3, column=1)

root.mainloop()

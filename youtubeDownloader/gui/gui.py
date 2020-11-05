import os
from tkinter import Tk, Label, Entry, Button, ttk

import youtubeDownloader.gui.get_widgets as gw

from youtubeDownloader.downloader.downloader_w_gui import Downloader


def intialize_downloader() -> None:
    """
    Initializes the Downloader obj.

    :return: None
    """

    dl = Downloader(
        address_entry.get(), quality_combobox.get(), filetype_combobox.get()
    )

    display_video_info(dl)
    dl.start_download()


def display_video_info(dl: Downloader) -> None:
    """
    Gets and displays the video info.

    :param dl: The downloader instance
    :return: None
    """

    gw.get_thumbnail(root, dl)
    gw.get_title(root, dl)
    gw.get_author(root, dl)
    gw.get_views(root, dl)
    gw.get_length(root, dl)
    gw.get_description(root, dl)


def on_closing() -> None:
    """
    Deletes all downloaded files to reduce clutter on close.

    :return: None
    """

    directory = "./youtubeDownloader/downloads"
    files = os.listdir(directory)
    for file in files:
        if file.endswith(".mp4") or file.endswith(".webm") \
                or file.endswith(".3gpp"):
            os.remove(os.path.join(directory, file))
    if len(os.listdir("./youtubeDownloader/tmp")) != 0:
        os.remove("./youtubeDownloader/tmp/tmp.jpg")
    root.destroy()


root = Tk()
root.title("Youtube Video Downloader")
root.geometry("520x400")
root.resizable(width=False, height=False)

address_label = Label(root, text="Video address:")
address_entry = Entry(root)

quality_label = Label(root, text="Resolution:")
quality_combobox = ttk.Combobox(
    root, values=["144p", "240p", "360p", "480p", "720p", "1080p"], state="readonly"
)
quality_combobox.current(4)

filetype_label = Label(root, text="Filetype:")
filetype_combobox = ttk.Combobox(root, values=["mp4", "webm", "3gpp"], state="readonly")
filetype_combobox.current(0)

submit_button = Button(root, text="Submit", command=intialize_downloader)

address_label.place(x=20, y=20)
address_entry.place(x=20, y=50, width=350)

quality_label.place(x=20, y=80)
quality_combobox.place(x=93, y=80, width=60)

filetype_label.place(x=250, y=80)
filetype_combobox.place(x=310, y=80, width=60)

submit_button.place(x=400, y=20, height=50, width=100)

root.protocol("WM_DELETE_WINDOW", on_closing)


def run() -> None:
    """
    Starts GUI loop.

    :return: None
    """
    root.mainloop()

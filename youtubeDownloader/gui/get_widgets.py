import urllib.request
from tkinter import Tk, Label, Text, END, WORD, DISABLED

from PIL import Image, ImageTk

from youtubeDownloader.downloader.downloader_w_gui import Downloader


def get_thumbnail(root: Tk, dl: Downloader) -> None:
    """
    Gets and displays the thumbnail.

    :param root: The tkinter instance
    :param dl: The downloader
    :return: None
    """

    urllib.request.urlretrieve(dl.thumbnail, "./youtubeDownloader/tmp/tmp.jpg")

    image = Image.open("./youtubeDownloader/tmp/tmp.jpg").resize(
        (160, 90), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)

    thumbnail = Label(root, image=photo)
    thumbnail.image = photo
    thumbnail.place(x=20, y=120)


def get_title(root: Tk, dl: Downloader) -> None:
    """
    Gets and displays the title.

    :param root: The tkinter instance
    :param dl: The downloader
    :return: None
    """

    title = Label(root, text=dl.title)
    title.place(x=200, y=120)


def get_author(root: Tk, dl: Downloader) -> None:
    """
    Gets and displays the author.

    :param root: The tkinter instance
    :param dl: The downloader
    :return: None
    """

    author_label = Label(root, text="Author:")
    author = Label(root, text=dl.author)

    author_label.place(x=200, y=150)
    author.place(x=250, y=150)


def get_views(root: Tk, dl: Downloader) -> None:
    """
    Gets and displays the view count.

    :param root: The tkinter instance
    :param dl: The downloader
    :return: None
    """

    view_label = Label(root, text="Views:")
    views = Label(root, text="{:,}".format(dl.views))

    view_label.place(x=380, y=180)
    views.place(x=420, y=180)


def get_length(root: Tk, dl: Downloader) -> None:
    """
    Gets and displays the length in seconds.

    :param root: The tkinter instance
    :param dl: The downloader
    :return: None
    """

    length_label = Label(root, text="Length:")
    length = Label(
        root,
        text="%02d:%02d:%02d"
        % (dl.length // 60 // 60, dl.length // 60, dl.length % 60),
    )

    length_label.place(x=200, y=180)
    length.place(x=250, y=180)


def get_description(root: Tk, dl: Downloader) -> None:
    """
    Gets and displays the description.

    :param root: The tkinter instance
    :param dl: The downloader
    :return: None
    """

    desc = Text(root, width=59, height=8, wrap=WORD)
    desc.place(x=20, y=240)
    desc.insert(END, dl.description)
    desc.config(state=DISABLED)

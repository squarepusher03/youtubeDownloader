from pytube import YouTube


class Downloader:
    def __init__(self, address: str, quality: str, extension: str) -> None:
        """
        Initializes a Downloader object.

        :param address: Address of the video
        :param quality: Resolution of the video
        :param extension: Extension type of the video
        """
        if address:
            self.address = address
            self.yt = YouTube(address.encode("unicode_escape").decode("utf-8"))
        else:
            address = "https://www.youtube.com/watch?v=vGHeStJ3Ibk"
            self.address = address
            self.yt = YouTube(address.encode("unicode_escape").decode("utf-8"))
        self.title = self.yt.title
        self.views = self.yt.views
        self.length = self.yt.length
        self.author = self.yt.author
        self.thumbnail = self.yt.thumbnail_url
        self.description = self.yt.description
        self.quality = quality
        self.extension = extension

        if len(self.title) > 50:
            self.title = self.title[:50]
            self.title += "..."

    def get_stream(self) -> str:
        """
        Gets the stream requested.

        :return: The Stream obj requested.
        """
        stream = self.yt.streams.filter(
            res=self.quality, file_extension=self.extension
        ).first()
        if not stream:
            stream = self.yt.streams.filter(res="360p", file_extension="mp4").first()
        return stream

    def start_download(self):
        if self.address != "https://www.youtube.com/watch?v=vGHeStJ3Ibk":
            self.get_stream().download("./downloads")

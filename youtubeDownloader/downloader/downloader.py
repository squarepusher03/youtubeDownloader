from pytube import YouTube


def take_input() -> YouTube:
    """
    Takes the user input and returns the video as a YouTube object.

    :return: YouTube object of link
    """
    video_link = input("Enter video address: ").encode("unicode_escape")
    video_link = video_link.decode("utf-8")
    return YouTube(video_link)


def find_stream(quality_index: int, yt: YouTube) -> str:
    """
    Returns the stream of the desired quality passed.

    :param quality_index: Index of the quality in the switch case
    :param yt: Instance of YouTube
    :return: the stream object of the desired quality
    """
    switcher = {1: "144p", 2: "240p", 3: "360p", 4: "480p", 5: "720p", 6: "1080p"}

    quality = switcher.get(quality_index, "360p")
    return yt.streams.filter(res=quality, file_extension="mp4").first()


def download(yt: YouTube) -> None:
    """
    Downloads the stream chosen.

    :param yt: Instance of YouTube
    :return: None
    """
    if input("Would you like to download this video (y/n): ") == "y":
        stream = find_stream(
            int(
                input(
                    """
                Enter the number of the quality you want: 

                1) 144p
                2) 240p
                3) 360p
                4) 480p
                5) 720p
                6) 1080p
                
                """
                )
            ),
            yt,
        )
        stream.download(".\downloads")
    else:
        return


def run_downloader() -> None:
    """
    Starts the downloader.

    :return: None
    """
    yt = take_input()
    print(
        f"""\n
            Video Title: {yt.title}
            Views: {yt.views}
            Length: {yt.length}
            Author: {yt.author}
            """
    )
    download(yt)

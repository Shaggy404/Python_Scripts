###Prerequite
### Pip install pytube

from pytube import YouTube

def video_downloader(video_url):
    my_video = YouTube(video_url)
    my_video.streams.get_highest_resolution().download()
    return my_video.title

try:
    youtube_link = input('Enter the youTube link: ')
    print(f'Downloading your video, please wait......')
    video = video_downloader(youtube_link)
    print(f'"{video}" downloaded successfully!!')

except:
    print(f'Failed to download video\nthe'\
        'following might be the causes\n->No internet'\
            'connection\n->Invalid video link')

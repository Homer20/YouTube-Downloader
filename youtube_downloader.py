from pytube import YouTube
from sys import argv

# Checking to see if 2 command line arguments are provided
try:
    # The second command line argument is the link of the video you want to download
    link = argv[1]

except IndexError:
    print("Expected 2 arguments")
    raise (SystemExit)

# Checking if the link is a youtube link
if "https://www.youtube.com" not in argv[1]:
    print("Expected a youtube link")
    raise (SystemExit)
        

# Making the link into a youtube object
youtube = YouTube(link)

# Printing information about the video
print("Title: ", youtube.title)
print("Views: ", youtube.views)
print("Length: ", youtube.length)
print("Publish date: ", youtube.publish_date)
print("Youtuber: ", youtube.author)

# Downloading the highest resolution video
youtube_downloads = youtube.streams.get_highest_resolution()

# The downloaded video will be in the folder you choose
youtube_downloads.download('C:/Users/dpate/OneDrive/Desktop/Youtube Downloads')
# initialize gui screen 

import tkinter
import pytube 
root = tkinter.Tk()

# set window size
root.geometry("400x400")

# set window background color
root.configure(bg="lightblue")

# set window minimum size
root.minsize(400, 400)

# set window title
root.title("youtube video downloader")

# set window icon
photo = tkinter.PhotoImage(file = 'youtube.png')
root.wm_iconphoto(False, photo)

# create label for window title
label = tkinter.Label(root, text = "Youtube video downloader", font = "Verdana 20 bold",bg="lightblue")
label.pack(padx = 10, pady = 10)

# create label for url

url_label = tkinter.Label(root, text = "Enter url", font = "Verdana 10 bold",bg="lightblue")
url_label.pack(padx = 10, pady = 10)

# create entry box

url_entry = tkinter.Entry(root, width = 50)
url_entry.pack(padx = 10, pady = 10)

def download_video(url):
    #create label for enter url 
    entered_url=tkinter.Label(root, text = f'You searched for \n {url}', font = "Verdana 10 bold",bg="lightblue")
    entered_url.pack(padx = 10, pady = 10)

    #download video
    yt = pytube.YouTube(url)
    video = yt.streams.first()
    print("downloading...")
    video.download()
    print("done")

def download_audio(url):
    #create label for enter url 
    entered_url=tkinter.Label(root, text = f'You searched for \n {url}', font = "Verdana 10 bold",bg="lightblue")
    entered_url.pack(padx = 10, pady = 10)

    #download video
    yt = pytube.YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    print("downloading...")
    video.download()
    print("done")

# create video download Button
download_button = tkinter.Button(root, text = "Download", font = "Verdana 10 bold",bg="lightblue", command = lambda: download_video(url_entry.get()))
download_button.pack(padx = 10, pady = 10)

# create audio download Button
audio_download_button= tkinter.Button(root, text = "Download audio", font = "Verdana 10 bold",bg="lightblue",command = lambda: download_audio(url_entry.get()))
audio_download_button.pack(padx = 10, pady = 10)

root.mainloop()
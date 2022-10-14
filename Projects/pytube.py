from pytube import YouTube

url = "https://www.youtube.com/watch?v=ID_L0aGI9bg"
YouTube(url).streams.get_highest_resolution().download()

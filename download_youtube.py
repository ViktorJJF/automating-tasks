import pytube

from sys import argv

link = input("Pega tu link de Youtube: ")
video = pytube.YouTube(link)
print("El titulo: ", video.title)
print("Vistas: ", video.views)
resolutions = video.streams.all()
for i in resolutions:
    print("Resolution:", i)

yd = video.streams.filter(only_audio=True).all()[0].download("./videos")

from rssagregator import RssAgr
from mp3play import PlayEp

rssobj = RssAgr("http://feeds.rucast.net/radio-t")
print(rssobj.eplist)
print(rssobj.eplist["Радио-Т 697"])

player = PlayEp(rssobj.eplist["Радио-Т 697"])
player.play
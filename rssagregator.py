import feedparser

class RssAgr():
    feedurl = ""
    eplist = {}

    def __init__(self, paramrssurl):
        print(paramrssurl)
        self.feedurl = paramrssurl
        self.eplist.clear
        self.parse()

    def parse(self):
        thefeed = feedparser.parse(self.feedurl)

        print("Список выпусков")
        print(thefeed.feed.get("title", thefeed.feed.title))

        for thefeedentry in thefeed.entries:
            title = thefeedentry.get("title", "")
            mediacontent = thefeedentry.get("media_content", "")
            self.eplist.update([(title, mediacontent[0]['url'])])



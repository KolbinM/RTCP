from playsound import playsound

class PlayEp():
    episode = ""
    
    def __init__(self, episodeUrl):
        print(episodeUrl)
        self.episode = episodeUrl
        
    def play(self):
        print("Plaing:")
        playsound(self.episode)
from .settings import Settings


class LastAmp:
    def __init__(self):
        self.dot = Settings()
        self.plex = self.dot.PlexAuth()

    def run(self):
        for video in self.plex.search("Dig"):
            print("%s (%s)" % (video.title, video.TYPE))

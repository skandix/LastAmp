import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.PLEX_TOKEN = os.environ.get("PLEX_TOKEN")
        self.PLEX_BASEURL = os.environ.get("PLEX_BASEURL")

        self.PLEX_USERNAME = os.environ.get("PLEX_USERNAME")
        self.PLEX_PASSWORD = os.environ.get("PLEX_PASSWORD")
        self.PLEX_SERVERNAME = os.environ.get("PLEX_SERVERNAME")

        self.LASTFM_CLIENT_KEY = os.environ.get("LASTFM_CLIENT_KEY")
        self.LASTFM_CLIENT_SECRET = os.environ.get("LASTFM_CLIENT_SECRET")

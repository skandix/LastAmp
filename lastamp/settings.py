import os

from dotenv import load_dotenv
from .modules._Datastructs import LastFMAuth, PlexAccountAuth, PlexServerAuth, asdict

load_dotenv()


class Settings:
    def __init__(self):
        self.__PLEX_TOKEN = os.environ.get("PLEX_TOKEN")
        self.__PLEX_BASEURL = os.environ.get("PLEX_BASEURL")

        self.__PLEX_USERNAME = os.environ.get("PLEX_USERNAME")
        self.__PLEX_PASSWORD = os.environ.get("PLEX_PASSWORD")
        self.__PLEX_SERVERNAME = os.environ.get("PLEX_SERVERNAME")

        self.__LASTFM_CLIENT_KEY = os.environ.get("LASTFM_CLIENT_KEY")
        self.__LASTFM_CLIENT_SECRET = os.environ.get("LASTFM_CLIENT_SECRET")

    def PlexAuth(self):
        if (
            self.__PLEX_USERNAME and self.__PLEX_PASSWORD and self.__PLEX_SERVERNAME
        ) == "" or None:
            return asdict(PlexServerAuth(self.__PLEX_TOKEN, self.__PLEX_BASEURL))
        elif (self.__PLEX_TOKEN and self.__PLEX_BASEURL) == "" or None:
            return asdict(
                PlexAccountAuth(
                    self.__PLEX_USERNAME, self.__PLEX_PASSWORD, self.__PLEX_SERVERNAME
                )
            )
        else:
            # TODO: create cleaner error msg and custom error to.
            raise ValueError(
                "Dupe Config, choose either account or server auth, or GTFO"
            )

    def LastFMAuth(self):
        return asdict(LastFMAuth(self.__LASTFM_CLIENT_KEY, self.__LASTFM_CLIENT_SECRET))

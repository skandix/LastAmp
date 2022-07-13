import os

from dotenv import load_dotenv
from plexapi.server import PlexServer
from plexapi.myplex import MyPlexAccount

from .modules._Datastructs import LastFMAuth, PlexAccountAuth, PlexServerAuth, asdict

load_dotenv()


class Settings:
    def __init__(self):
        self.__PLEX_TOKEN = os.environ.get("PLEX_TOKEN")
        self.__PLEX_BASEURL = os.environ.get("PLEX_BASEURL")
        self.__PLEX_AUTH_SERVER = PlexServerAuth(self.__PLEX_TOKEN, self.__PLEX_BASEURL)

        self.__PLEX_USERNAME = os.environ.get("PLEX_USERNAME")
        self.__PLEX_PASSWORD = os.environ.get("PLEX_PASSWORD")
        self.__PLEX_SERVERNAME = os.environ.get("PLEX_SERVERNAME")
        self.__PLEX_AUTH_ACCOUNT = PlexAccountAuth(
            self.__PLEX_USERNAME, self.__PLEX_PASSWORD, self.__PLEX_SERVERNAME
        )

        self.__LASTFM_CLIENT_KEY = os.environ.get("LASTFM_CLIENT_KEY")
        self.__LASTFM_CLIENT_SECRET = os.environ.get("LASTFM_CLIENT_SECRET")
        self.__LASTFM_API_AUTH = LastFMAuth(
            self.__LASTFM_CLIENT_KEY, self.__LASTFM_CLIENT_SECRET
        )

    def PlexAuth(self):
        if (
            self.__PLEX_USERNAME and self.__PLEX_PASSWORD and self.__PLEX_SERVERNAME
        ) != "":
            __ACCOUNT = MyPlexAccount(
                self.__PLEX_AUTH_ACCOUNT.PLEX_USERNAME,
                self.__PLEX_AUTH_ACCOUNT.PLEX_PASSWORD,
            )
            __PLEX = __ACCOUNT.resource(
                self.__PLEX_AUTH_ACCOUNT.PLEX_SERVERNAME
            ).connect()
            return __PLEX
        elif (self.__PLEX_TOKEN and self.__PLEX_BASEURL) != "":
            __PLEX = PlexServer(
                self.__PLEX_AUTH_SERVER.PLEX_BASEURL, self.__PLEX_AUTH_SERVER.PLEX_TOKEN
            )
            return __PLEX
        else:
            # TODO: create cleaner error msg and custom error to.
            raise ValueError(
                "Dupe Config, choose either account or server auth, or GTFO"
            )

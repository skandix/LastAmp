from dataclasses import dataclass, asdict


@dataclass(repr=True)
class PlexServerAuth:
    PLEX_TOKEN: str
    PLEX_BASEURL: str


@dataclass
class PlexAccountAuth:
    PLEX_USERNAME: str
    PLEX_PASSWORD: str
    PLEX_SERVERNAME: str


@dataclass
class LastFMAuth:
    LASTFM_CLIENT_KEY: str
    LASTFM_CLIENT_SECRET: str

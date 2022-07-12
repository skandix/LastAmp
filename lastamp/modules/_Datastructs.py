from dataclasses import dataclass, asdict


@dataclass(repr=True)
class VideoStruct:
    PresentationID: str
    Author: str
    VideoFile: str
    VideoTitle: str
    PlayerID: str
    UsedInCourse: str


@dataclass
class PanoptoMetaStruct:
    Folder_ID: str
    Owner: str
    VideoFile: str
    Panopto_ID: str


@dataclass
class MediasiteMetaStruct:
    Author: str
    PresentationID: str
    VideoFile: str
    VideoTitle: str
    UsedInCourse: str


@dataclass()
class UploadMetadata:
    Panopto: PanoptoMetaStruct
    Mediasite: MediasiteMetaStruct

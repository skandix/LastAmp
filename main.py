#!/usr/bin/env python3
from lastamp.lastamp import LastAmp

la = LastAmp()
last = la.dot.LastFMAuth()
plex = la.dot.PlexAuth()
print(f"{last=}\n{plex=}")

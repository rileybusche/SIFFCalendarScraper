from enum import StrEnum


# the string value must match the one used in the SIFF website URL
class SIFFTheatre(StrEnum):
    EGYPTIAN = "siff-cinema-egyptian"
    DOWNTOWN = "siff-cinema-downtown"
    UPTOWN = "siff-cinema-uptown"
    FILM_CENTER = "siff-film-center"


class GoogleCalendar(StrEnum):
    SIFF_CINEMA_EGYPTIAN = "d9ad77d20a018d11c20560b1ceb55b92c5b64ee10b322ac2c7da39e178aa17fc@group.calendar.google.com"
    SIFF_CINEMA_DOWNTOWN = "a03eefa417a8c79ec4d4007ef921a99c601966da78b241fee2e1bfa6594f05b5@group.calendar.google.com"
    SIFF_CINEMA_UPTOWN = "4c6a8cd33ce0148926c3cead5c526497396c748e867529680ac42a433301be4c@group.calendar.google.com"
    SIFF_FILM_CENTER = "dbd809e897c3d7a8f2f13a63d3549d5141d4f848201ad1824daa61ec35769591@group.calendar.google.com"

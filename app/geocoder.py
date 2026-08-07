from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError
from timezonefinder import TimezoneFinder

_tf = TimezoneFinder()

# Stable locations for the built-in demo personalities. All other city inputs
# continue through Nominatim.
DEMO_LOCATIONS = {
    "Los Angeles, Estados Unidos": (34.0522, -118.2437, "America/Los_Angeles"),
    "Gary, Indiana, Estados Unidos": (41.5934, -87.3464, "America/Chicago"),
    "Aberdeen, Washington, Estados Unidos": (46.9754, -123.8157, "America/Los_Angeles"),
    "Mvezo, África do Sul": (-31.9455, 28.5125, "Africa/Johannesburg"),
    "Brooklyn, Nova York, Estados Unidos": (40.6782, -73.9442, "America/New_York"),
    "Porbandar, Índia": (21.6417, 69.6293, "Asia/Kolkata"),
    "Coyoacán, Cidade do México, México": (19.3467, -99.1617, "America/Mexico_City"),
    "Londres, Inglaterra": (51.5072, -0.1276, "Europe/London"),
    "Sandringham, Inglaterra": (52.8300, 0.5100, "Europe/London"),
    "Ulm, Alemanha": (48.4011, 9.9876, "Europe/Berlin"),
    "Honolulu, Havaí, Estados Unidos": (21.3069, -157.8583, "Pacific/Honolulu"),
    "Hope, Arkansas, Estados Unidos": (33.6671, -93.5916, "America/Chicago"),
    "Queens, Nova York, Estados Unidos": (40.7282, -73.7949, "America/New_York"),
    "Scranton, Pensilvânia, Estados Unidos": (41.4090, -75.6624, "America/New_York"),
    "Tampico, Illinois, Estados Unidos": (40.6300, -89.7900, "America/Chicago"),
    "Brookline, Massachusetts, Estados Unidos": (42.3318, -71.1212, "America/New_York"),
    "Hyde Park, Nova York, Estados Unidos": (41.7851, -73.9337, "America/New_York"),
    "Tupelo, Mississippi, Estados Unidos": (34.2576, -88.7034, "America/Chicago"),
    "Kosciusko, Mississippi, Estados Unidos": (33.0585, -89.5876, "America/Chicago"),
    "Atlanta, Geórgia, Estados Unidos": (33.7490, -84.3880, "America/New_York"),
}


def resolve_location(city):
    """City name -> (lat, lon, tz_str).

    Auto-derives the IANA timezone from the coordinates so callers only need to
    supply a city. Raises LookupError if the city or its timezone can't be found.
    """
    if city in DEMO_LOCATIONS:
        return DEMO_LOCATIONS[city]

    geolocator = Nominatim(user_agent="astrolens")
    try:
        location = geolocator.geocode(city)
    except GeocoderServiceError as exc:
        raise ConnectionError("Location service is temporarily unavailable") from exc
    if location is None:
        raise LookupError("Não foi possível localizar a cidade informada.")

    lat, lon = location.latitude, location.longitude
    try:
        tz = _tf.timezone_at(lng=lon, lat=lat)
    except Exception as exc:
        raise ConnectionError("Location service is temporarily unavailable") from exc
    if tz is None:
        raise LookupError("Não foi possível determinar o fuso horário da cidade informada.")

    return lat, lon, tz

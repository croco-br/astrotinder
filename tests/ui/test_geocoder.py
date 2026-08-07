import asyncio

from geopy.exc import GeocoderUnavailable

from app import geocoder
from app import main
from app.models import ChartRequest


def test_resolve_location_wraps_service_failures(monkeypatch):
    class UnavailableGeocoder:
        def geocode(self, city):
            raise GeocoderUnavailable("offline")

    monkeypatch.setattr(geocoder, "Nominatim", lambda user_agent: UnavailableGeocoder())

    try:
        geocoder.resolve_location("São Paulo, Brasil")
    except ConnectionError as exc:
        assert str(exc) == "Location service is temporarily unavailable"
    else:
        raise AssertionError("expected service failure to be wrapped")


def test_demo_location_does_not_call_geocoder(monkeypatch):
    monkeypatch.setattr(
        geocoder,
        "Nominatim",
        lambda user_agent: (_ for _ in ()).throw(AssertionError("should not geocode demo")),
    )

    assert geocoder.resolve_location("Los Angeles, Estados Unidos") == (
        34.0522, -118.2437, "America/Los_Angeles"
    )


def test_unknown_location_does_not_reflect_input(monkeypatch):
    class MissingGeocoder:
        def geocode(self, city):
            return None

    monkeypatch.setattr(geocoder, "Nominatim", lambda user_agent: MissingGeocoder())

    try:
        geocoder.resolve_location("<script>alert(1)</script>")
    except LookupError as exc:
        assert str(exc) == "Não foi possível localizar a cidade informada."
    else:
        raise AssertionError("expected missing location to raise")


def test_calculate_returns_503_for_location_service_failure(monkeypatch):
    def unavailable(*args, **kwargs):
        raise ConnectionError("Location service is temporarily unavailable")

    monkeypatch.setattr(main, "calculate_chart", unavailable)
    response = asyncio.run(main.calculate(ChartRequest(
        date="1990-01-01", time="12:00", city="São Paulo, Brasil"
    )))

    assert response.status_code == 503
    assert response.body == b'{"error":"Location service is temporarily unavailable"}'

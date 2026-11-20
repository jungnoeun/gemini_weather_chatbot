
import requests


def get_weather(location: str) -> dict:
    """지정한 지역의 현재 날씨를 조회합니다.

    Args:
        location: 도시와 국가 이름. 예: Seoul, South Korea
    """

    print(f"\n[함수 호출] get_weather({location})")

    # 1. 지역 이름을 위도·경도로 변환
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_response = requests.get(
        geo_url,
        params={
            "name": location,
            "count": 1,
            "language": "ko"
        },
        timeout=10
    )
    geo_response.raise_for_status()

    locations = geo_response.json().get("results", [])

    if not locations:
        return {
            "error": f"'{location}' 지역을 찾을 수 없습니다."
        }

    place = locations[0]

    latitude = place["latitude"]
    longitude = place["longitude"]

    matched_name = (
        f"{place['name']}, "
        f"{place.get('admin1', '')}, "
        f"{place.get('country', '')}"
    )

    print(f"[검색된 지역] {matched_name}")

    # 2. 해당 좌표의 현재 날씨 조회
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_response = requests.get(
        weather_url,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "apparent_temperature",
                "precipitation",
                "wind_speed_10m",
                "weather_code"
            ],
            "timezone": "auto"
        },
        timeout=10
    )
    weather_response.raise_for_status()

    current = weather_response.json()["current"]

    # 3. 조회 결과 반환
    return {
        "location": matched_name,
        "time": current["time"],
        "temperature_c": current["temperature_2m"],
        "feels_like_c": current["apparent_temperature"],
        "humidity_percent": current["relative_humidity_2m"],
        "precipitation_mm": current["precipitation"],
        "wind_speed_kmh": current["wind_speed_10m"],
        "weather_code": current["weather_code"]
    }

import requests
import os

CLIENT_ID = os.getenv("STRAVA_CLIENT_ID", "YOUR_CLIENT_ID")
CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET", "YOUR_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8501"


def authenticate_strava():
    auth_url = (
        f"https://www.strava.com/oauth/authorize?client_id={CLIENT_ID}"
        f"&response_type=code&redirect_uri={REDIRECT_URI}&approval_prompt=force&scope=activity:read_all"
    )
    return auth_url


def fetch_activities(auth_code):
    token_url = "https://www.strava.com/oauth/token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": auth_code,
        "grant_type": "authorization_code",
    }
    response = requests.post(token_url, data=payload)
    access_token = response.json().get("access_token")

    headers = {"Authorization": f"Bearer {access_token}"}
    activities_url = "https://www.strava.com/api/v3/athlete/activities"
    params = {"per_page": 200, "page": 1}
    response = requests.get(activities_url, headers=headers, params=params)

    activities = response.json()

    # Filtrar apenas Rides (MTB outdoor)
    rides = [
        {
            "id": act["id"],
            "name": act["name"],
            "distance": act["distance"] / 1000,  # metros para km
            "moving_time": act["moving_time"],
            "elapsed_time": act["elapsed_time"],
            "total_elevation_gain": act["total_elevation_gain"],
            "start_date": act["start_date"]
        }
        for act in activities if act["type"] == "Ride"
    ]
    return rides

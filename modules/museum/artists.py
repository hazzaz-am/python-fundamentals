import requests


def get_artists(query, limit):
    try:
        res = requests.get(
            "https://api.artic.edu/api/v1/agents/search", {"q": query, "limit": limit}
        )
        res.raise_for_status()
    except requests.HTTPError:
        return []

    content = res.json()
    return [artist["title"] for artist in content["data"]]

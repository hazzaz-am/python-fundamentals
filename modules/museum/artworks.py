import requests


def get_artworks(query, limit):
    try:
        res = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": query, "limit": limit}
        )
        res.raise_for_status()
    except requests.HTTPError:
        return []

    content = res.json()
    return [artwork["title"] for artwork in content["data"]]

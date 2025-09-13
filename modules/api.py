from museum.artworks import get_artworks
from museum.artists import get_artists


def main():
    artist = input("Enter Artworks: ")
    agent = input("Enter Agents: ")

    artworks = get_artworks(artist, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")

    agents = get_artists(artist, limit=3)
    for agent in agents:
        print(f"* {agent}")


main()

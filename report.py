def main():
    space_craft_1 = {"name": "Voyager 1", "distance": 163}
    space_craft_2 = {"name": "James Telescope"}

    space_craft_2["distance"] = 0.01
    space_craft_1.update({"distance": 160})
    space_craft_2.update({"orbit": "Sun"})

    print(create_report(space_craft_1))
    print(create_report(space_craft_2))


def create_report(space_craft):
    return f"""
  Name: {space_craft["name"]}
  Disance: {space_craft.get("distance", "Unknown")} AU
  Orbit: {space_craft.get("orbit", "Unknown")}
  """


main()

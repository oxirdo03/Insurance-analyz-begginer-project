name = [{"name": "north", "people": 20}, {"name": "south", "people": 32}]

for line in name:
    if line["name"] == "north":
        print(line["people"])

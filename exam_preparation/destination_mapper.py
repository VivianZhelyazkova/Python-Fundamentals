import re

places = input()

regex = r"([=\/]){1}([A-Z]{1}[a-zA-Z]{2,})\1"
matches = re.finditer(regex, places)
destinations = []
travel_points = 0
for match in matches:
    destinations.append(match.group(2))
    travel_points += len(match.group(2))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
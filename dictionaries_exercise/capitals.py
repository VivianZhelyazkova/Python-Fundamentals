# countries = input().split(", ")
# capitals = input().split(", ")

# my_dict = dict(zip(input().split(", "), input().split(", ")))
my_dict2 = {key: value for key, value in zip(input().split(", "), input().split(", "))}
for country, capital in my_dict2.items():
    print(f"{country} -> {capital}")

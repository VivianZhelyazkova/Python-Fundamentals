beach = input()
#
# my_list = ["sand", "water", "fish", "sun"]

lowercase_beach = beach.lower()

sand_count = lowercase_beach.count("sand")
water_count = lowercase_beach.count("water")
fish_count = lowercase_beach.count("fish")
sun_count = lowercase_beach.count("sun")
total = sand_count + fish_count + sun_count + water_count
print(total)
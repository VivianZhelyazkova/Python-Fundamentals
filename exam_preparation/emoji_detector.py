import math
import re

text = input()

numbers = list(int(x) for x in text if x.isnumeric())
threshold = math.prod(numbers)
print(threshold)

lines = int(input())
positives = []
negatives = []
# positives_count = 0
# negatives_sum = 0

for line in range(lines):
    number = int(input())
    if number >= 0:
        positives.append(number)
        # positives_count += 1
    else:
        negatives.append(number)
        # negatives_sum += number

print(f"{positives}\n"
      f"{negatives}\n"
      f"Count of positives: {len(positives)}\n"
      f"Sum of negatives: {sum(negatives)}")
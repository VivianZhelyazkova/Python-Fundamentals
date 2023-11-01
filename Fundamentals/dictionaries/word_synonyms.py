number = int(input())
synonyms = {}

for _ in range(number):
    key = input()
    value = input()
    if key not in synonyms:
        synonyms[key] = []
    synonyms[key].append(value)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
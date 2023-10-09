list_of_words = [x for x in input().split() if x == x[::-1]]
palindrome = input()

print(list_of_words)
print(f"Found palindrome {list_of_words.count(palindrome)} times")

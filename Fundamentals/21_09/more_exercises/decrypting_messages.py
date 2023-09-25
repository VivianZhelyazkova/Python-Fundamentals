key = int(input())
number_of_lines = int(input())
word = ""
for line in range(number_of_lines):
    letter = input()
    letter_as_number = ord(letter)
    decrypted_letter_as_number = ord(letter) + key
    decrypted_letter = chr(decrypted_letter_as_number)
    word += decrypted_letter

print(word)
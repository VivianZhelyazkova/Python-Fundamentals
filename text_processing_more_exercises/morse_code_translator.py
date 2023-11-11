MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
}
reversed_morse_code_dict = {v: k for k, v in MORSE_CODE_DICT.items()}

message = input().split(" | ")
new_message = ""

for word in message:
    word = word.split()
    for letter in word:
        if letter in reversed_morse_code_dict:
            new_message += reversed_morse_code_dict[letter]
    new_message += " "
print(new_message)
string = input()
counter = int(input())

# result = lambda strng, number: strng * number
# final_result = result(string, counter)


def repeat(strng, number):
    result = strng * number
    return result


print(repeat(string, counter))


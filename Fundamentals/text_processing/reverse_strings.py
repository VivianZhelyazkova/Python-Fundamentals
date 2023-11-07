string = input()

while string != "end":
    # reversed_list = [char for char in reversed(string)]
    # reversed_string = "".join(reversed_list)
    # print(f"{string} = {reversed_string}")

    # reversed_list = list(string)
    # reversed_list.reverse()
    # reversed_string = "".join(reversed_list)
    # print(f"{string} = {reversed_string}")

    reversed_string = "".join(reversed(string))
    print(f"{string} = {reversed_string}")
    string = input()



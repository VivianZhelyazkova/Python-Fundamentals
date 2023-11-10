tickets = input()
tickets = tickets.replace(" ", "")
tickets = tickets.split(",")


def symbol_counter(symbol, half):
    counter = 0
    max_count = 0
    for symb in half:
        if symb == symbol:
            counter += 1

        else:
            max_count = max(max_count, counter)
            counter = 0
    return max(max_count, counter)


def is_winning(count_one, count_two):
    return count_one in range(6, 11) and count_two in range(6, 11)


def is_jackpot(count_one, count_two):
    return count_one == 10 and count_two == 10


def evaluate_ticket(first_part, second_part, lottery_ticket):
    is_winner = False
    is_jack = False
    winning_symbols = ['@', '#', '$', '^']

    for character in winning_symbols:
        first_count = symbol_counter(character, first_part)
        second_count = symbol_counter(character, second_part)
        if is_jackpot(first_count, second_count):
            is_jack = True
            print(f'ticket "{lottery_ticket}" - {first_count}{character} Jackpot!')
        elif is_winning(first_count, second_count):
            is_winner = True
            print(f'ticket "{lottery_ticket}" - {min(first_count, second_count)}{character}')

    if not is_jack and not is_winner:
        print(f'ticket "{lottery_ticket}" - no match')


for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    first_half = ticket[:len(ticket) // 2]
    second_half = ticket[len(ticket) // 2:]

    evaluate_ticket(first_half, second_half, ticket)

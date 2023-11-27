list_of_times = input().split(" ")

left_player = list_of_times[:len(list_of_times) // 2]
right_player = list_of_times[(len(list_of_times) // 2) + 1:]
right_player.reverse()


def total_time(player):
    sum_of_times = 0
    for number in player:
        sum_of_times += int(number)
        if number == "0":
            sum_of_times *= 0.80
    return sum_of_times


left_player_time = total_time(left_player)
right_player_time = total_time(right_player)

if left_player_time < right_player_time:
    print(f"The winner is left with total time: {left_player_time:.1f}")
else:
    print(f"The winner is right with total time: {right_player_time:.1f}")


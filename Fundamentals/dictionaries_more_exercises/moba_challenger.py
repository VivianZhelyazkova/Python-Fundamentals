command = input()
players = {}

while command != "Season end":

    if "->" in command:
        player, position, skill = command.split(" -> ")
        if player not in players:
            players[player] =
    else:
        player_one, player_two = command.split("vs")

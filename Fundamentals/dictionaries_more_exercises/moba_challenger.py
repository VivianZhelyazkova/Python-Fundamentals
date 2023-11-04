command = input()
players = {}

while command != "Season end":

    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in players:
            players[player] = {position: skill}
        elif position not in players[player]:
            players[player][position] = skill
        elif skill > players[player][position]:
            players[player][position] = skill

    else:
        player_one, player_two = command.split("vs")
    command = input()

for player, info in players.items():
    total_points = 0
    for position, skill in info.items():
        total_points += skill
    print(f"{player}: {total_points}")
    for position, skill in info.items():
        print(f"- {position} <::> {skill}")

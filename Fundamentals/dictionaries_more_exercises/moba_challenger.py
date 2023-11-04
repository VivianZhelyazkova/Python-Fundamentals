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
        player_one, player_two = command.split(" vs ")
        if player_one in players and player_two in players:
            demoted_player = None
            for pos in players[player_one].keys():
                for p in players[player_two].keys():
                    if pos == p:
                        if sum(players[player_one].values()) > sum(players[player_two].values()):
                            demoted_player = player_two
                        elif sum(players[player_one].values()) < sum(players[player_two].values()):
                            demoted_player = player_one
            if demoted_player:
                players.pop(demoted_player)

    command = input()

sorted_skills = dict(sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0])))

for player, info in sorted_skills.items():
    print(f"{player}: {sum(info.values())} skill")
    sorted_names = dict(sorted(info.items(), key=lambda x: (-x[1], x[0])))
    for position, skill in sorted_names.items():
        print(f"- {position} <::> {skill}")

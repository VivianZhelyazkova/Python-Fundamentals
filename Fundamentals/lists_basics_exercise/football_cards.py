cards = input()
cards_list = cards.split(' ')

team_a_cards = set()
team_b_cards = set()

for card in cards_list:
    team = card.split('-')[0]
    # player = team.split('-')[1]
    if team == "A":
        team_a_cards.add(card)
    elif team == "B":
        team_b_cards.add(card)
    if (11 - len(team_a_cards)) < 7 or (11 - len(team_b_cards)) < 7:
        break

team_a_players = 11 - len(team_a_cards)
team_b_players = 11 - len(team_b_cards)

print(f"Team A - {team_a_players}; Team B - {team_b_players}")

if team_a_players < 7 or team_b_players < 7:
    print("Game was terminated")


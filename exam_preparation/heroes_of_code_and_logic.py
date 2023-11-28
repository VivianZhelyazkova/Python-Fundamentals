number_of_heroes = int(input())
heroes = {}
HP = 0
MP = 1
MAX_HP = 100
MAX_MP = 200

for line in range(number_of_heroes):
    hero = input()
    name, hp, mp = hero.split()
    hp = int(hp)
    mp = int(mp)
    heroes[name] = [hp, mp]

command = input()

while command != "End":

    if "CastSpell" in command:
        cmd, name, mp_needed, spell_name = command.split(" - ")
        mp_needed = int(mp_needed)
        if heroes[name][MP] >= mp_needed:
            heroes[name][MP] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name][MP]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif "TakeDamage" in command:
        cmd, name, damage, attacker = command.split(" - ")
        damage = int(damage)
        if heroes[name][HP] <= damage:
            print(f"{name} has been killed by {attacker}!")
            heroes.pop(name)
        else:
            heroes[name][HP] -= damage
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][HP]} HP left!")

    elif "Recharge" in command:
        cmd, name, amount = command.split(" - ")
        amount = int(amount)
        mp_received = MAX_MP - heroes[name][MP]
        heroes[name][MP] += amount
        if heroes[name][MP] > MAX_MP:
            heroes[name][MP] = MAX_MP
            amount = mp_received
        print(f"{name} recharged for {amount} MP!")

    elif "Heal" in command:
        cmd, name, amount = command.split(" - ")
        amount = int(amount)
        hp_received = MAX_HP - heroes[name][HP]
        heroes[name][HP] += amount
        if heroes[name][HP] > MAX_HP:
            heroes[name][HP] = MAX_HP
            amount = hp_received
        print(f"{name} healed for {amount} HP!")
    command = input()

for hero, stats in heroes.items():
    print(f"{hero}\n"
          f"  HP: {stats[HP]}\n"
          f"  MP: {stats[MP]}")

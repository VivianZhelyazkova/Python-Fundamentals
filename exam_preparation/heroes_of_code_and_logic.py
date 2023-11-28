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


def recharge_or_heal(string, my_heroes, command_type, resource):
    cmd, name, amount = string.split(" - ")
    amount = int(amount)
    mp_received = (MAX_MP if resource == MP else MAX_HP) - my_heroes[name][resource]
    my_heroes[name][resource] += amount
    if my_heroes[name][resource] > (MAX_MP if resource == MP else MAX_HP):
        my_heroes[name][resource] = (MAX_MP if resource == MP else MAX_HP)
        amount = mp_received
    string_resource = "HP" if resource == HP else "MP"
    print(f"{name} {command_type} for {amount} {string_resource}!")


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
        if damage >= heroes[name][HP]:
            print(f"{name} has been killed by {attacker}!")
            heroes.pop(name)
        else:
            heroes[name][HP] -= damage
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][HP]} HP left!")

    elif "Recharge" in command:
        recharge_or_heal(command, heroes, "recharged", MP)

    elif "Heal" in command:
        recharge_or_heal(command, heroes, "healed", HP)
    command = input()

for hero, stats in heroes.items():
    print(f"{hero}\n"
          f"  HP: {stats[HP]}\n"
          f"  MP: {stats[MP]}")

lessons = input().split(", ")
command = input()

while command != "course start":
    command = command.split(":")
    cmd = command[0]
    title = command[1]
    exercise = title + "-Exercise"
    if "Add" == cmd:
        if title not in lessons:
            lessons.append(title)
    elif "Insert" == cmd:
        index = int(command[2])
        if index < len(lessons):
            if title not in lessons:
                lessons.insert(index, title)
    elif "Remove" == cmd:
        if title in lessons:
            lessons.remove(title)
            if exercise in lessons:
                lessons.remove(exercise)
    elif "Swap" == cmd:
        first_title = command[1]
        second_title = command[2]
        second_exercise = second_title + "-Exercise"
        if first_title and second_title in lessons:
            first_index = lessons.index(first_title)
            second_index = lessons.index(second_title)
            if exercise in lessons and second_exercise in lessons:
                lessons[first_index], lessons[second_index] = lessons[second_index], lessons[first_index]
                lessons.remove(exercise)
                lessons.remove(second_exercise)
                lessons.insert(second_index + 1, exercise)
                lessons.insert(first_index + 1, second_exercise)
            elif exercise in lessons:
                lessons[first_index], lessons[second_index] = lessons[second_index], lessons[first_index]
                lessons.remove(exercise)
                lessons.insert(second_index + 1, exercise)
            elif second_exercise in lessons:
                lessons[first_index], lessons[second_index] = lessons[second_index], lessons[first_index]
                lessons.remove(second_exercise)
                lessons.insert(first_index + 1, second_exercise)
            else:
                lessons[first_index], lessons[second_index] = lessons[second_index], lessons[first_index]
    elif "Exercise" == cmd:
        if title not in lessons:
            if exercise not in lessons:
                lessons.append(title)
                lessons.append(exercise)
        else:
            if exercise not in lessons:
                index = lessons.index(title)
                lessons.insert(index + 1, exercise)
    command = input()

for n in range(len(lessons)):
    print(f"{n + 1}.{lessons[n]}")
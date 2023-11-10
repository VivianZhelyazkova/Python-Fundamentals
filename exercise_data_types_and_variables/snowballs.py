snowballs_count = int(input())

top_ball = {
    "weight": 0,
    "time": 0,
    "quality": 0,
    "value": 0
}
for snowball in range(snowballs_count):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if snowball_value > top_ball.get("value"):
        top_ball.update({"value": snowball_value})
        top_ball.update({"time": snowball_time})
        top_ball.update({"quality": snowball_quality})
        top_ball.update({"weight": snowball_weight})

print(f"{top_ball['weight']} : {top_ball['time']} = {int(top_ball['value'])} ({top_ball['quality']})")


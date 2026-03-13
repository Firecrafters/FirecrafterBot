from discord.ext.commands import Context

import commands.fish.catches as catches
import random

def get_random_rarity():
    random_value = random.random()
    cumulative_probability = 0

    for rarity in catches.RARITIES:
        cumulative_probability += rarity["probability"]
        if random_value < cumulative_probability:
            return rarity

    return catches.RARITIES[0]

def fish(context: Context):
    rarity = get_random_rarity()
    item = random.choice(catches.CATCHES)

    worth = item["value"] * rarity["multiplier"]

    if rarity["name"] == "uncommon":
        suffix = "n"
    else:
        suffix = ""

    print(f"{context.author.name} caught a {item["name"]} of rarity {rarity["name"]}")
    print(f"{context.author.name} gained {worth} points\n")
    return f"You caught a{suffix} {rarity["name"]} {item["name"]}\n+{worth} points"
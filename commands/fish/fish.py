from discord.ext.commands import Context
import sqlite3
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

    try:
        connection = sqlite3.connect("db.sqlite")
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS fishing_data (userID INTEGER PRIMARY KEY, username TEXT, points DECIMAL)')
        cursor.execute("INSERT INTO fishing_data (userID, username, points) VALUES (?, ?, ?) "
                       "ON CONFLICT (userID) "
                       "DO UPDATE SET points = fishing_data.points + EXCLUDED.points",
                       (context.author.id, context.author.name, worth))

        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            connection.close()

    if rarity["name"] == "uncommon":
        suffix = "n"
    else:
        suffix = ""

    print(f"{context.author.name} caught a {item["name"]} of rarity {rarity["name"]}")
    print(f"{context.author.name} gained {int(worth)} points ({item["value"]} * {rarity["multiplier"]})\n")
    return f"You caught a{suffix} {rarity["name"]} {item["name"]}\n+{int(worth)} points"

def get_points(context: Context):
    points = 0
    try:
        connection = sqlite3.connect("db.sqlite")
        cursor = connection.cursor()
        cursor.execute("SELECT points FROM fishing_data WHERE userID = ?", (context.author.id,))
        row = cursor.fetchone()
        if row:
            points = row[0]
            
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            connection.close()
    return f"You have {points} points"
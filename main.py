import os
import sys
import subprocess

import discord
from discord.ext import commands
from discord.ext.commands import Context
from dotenv import load_dotenv
from commands.fish.fish import fish as fish_func
from commands.fish.fish import get_points
import emotes

load_dotenv()

bot = commands.Bot(command_prefix="_", intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(name="fish")
async def fish(ctx: Context):
    await ctx.reply(fish_func(ctx))

@bot.command(name="points")
async def points(ctx: Context):
    await ctx.reply(get_points(ctx))

@bot.command(name="send")
async def send(ctx: Context):
    await ctx.send(ctx.message.content.split(f"{bot.command_prefix}send ")[1])

@bot.command(name="restart")
@commands.is_owner()
async def restart(ctx: Context):
    await ctx.reply(f"Restarting {emotes.CERBER_LOADING}")
    print("Restarting the bot...")
    subprocess.Popen([sys.executable] + sys.argv, creationflags=subprocess.CREATE_NEW_CONSOLE)
    os._exit(0)

@bot.command(name="help")
async def help(ctx: Context):
    await ctx.reply(f"{emotes.NO} elp")

@bot.command(name="stop")
async def stop(ctx: Context):
    await ctx.reply(f"Stopping {emotes.CERBER_LOADING}")
    print("Stopping the bot...")
    os._exit(0)

bot.run(os.getenv("TOKEN"))
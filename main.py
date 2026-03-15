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

async def send_online_msg(target_channel_id):
    channel = bot.get_channel(target_channel_id)

    if channel and isinstance(channel, discord.TextChannel):
        await channel.send(f"{emotes.ONLINE} Online")
    else:
        print(f"Error: Channel {target_channel_id} not found")

@bot.event
async def on_ready():
    await bot.wait_until_ready()

    print(f"Logged in as {bot.user}\n")

    channel_1_specified = False
    channel_2_specified = False

    if os.getenv("ONLINE_CHANNEL_1") != "off":
        channel_1_specified = True
        target_channel_id_1 = int(os.getenv("ONLINE_CHANNEL_1"))
    if os.getenv("ONLINE_CHANNEL_2") != "off":
        channel_2_specified = True
        target_channel_id_2 = int(os.getenv("ONLINE_CHANNEL_2"))

    if channel_1_specified:
        await send_online_msg(target_channel_id_1)
    if channel_2_specified:
        await send_online_msg(target_channel_id_2)

@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    command_list = []
    for command in bot.commands:
        command_list.append(command.name)

    if message.author.bot:
        for commandName in command_list:
            if message.content.startswith(f"{bot.command_prefix}{commandName}"):
                my_command = bot.get_command(f"{commandName}")
                ctx = await bot.get_context(message)
                await my_command.invoke(ctx)


    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx: Context, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply(emotes.NO)

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
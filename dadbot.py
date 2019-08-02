import asyncio
import config
import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix=config.prefix,
          description=config.description,
          activity=discord.Game(config.game))

@bot.event
async def on_ready():
    print('Connected as: {}'.format(bot.user.name))
    print('Discord.py Version: {}'.format(discord.__version__))

@bot.event
async def on_server_join(server):
    print('Added to server: {}'.format(server.name))

@bot.event
async def on_server_leave(server):
    print('Removed from server: {}'.format(server.name))

@bot.event
async def on_message(message):
    triggers = ("im", "i'm")
    for trigger in triggers:
        if message.content.lower().startswith(trigger + ' '):
            await message.channel.send("Hi {0}, I'm Dad".format(message.content[len(trigger):].strip()))
            break


bot.run(config.token)

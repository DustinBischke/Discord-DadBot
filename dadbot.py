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
    triggers = ["im", "i'm", 'i am']
    for trigger in triggers:
        if message.content.lower().startswith(trigger + ' '):
            content = message.content[len(trigger):].strip()
            if content.lower() == 'dad':
                await message.channel.send("You're not dad, I'm Dad!")
            else:
                await message.channel.send("Hi {0}, I'm Dad".format(content))
            break


bot.run(config.token)

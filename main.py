import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

discord.http.API_VERSION = 9

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1

	print("reminder racoon is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        if message.content == 'who is nishtha?':
            await message.channel.send("Nishtha is gandi bacchi")



bot.run(DISCORD_TOKEN)
import discord
from discord import app_commands 
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord.ext import commands
from addRemainder import add


load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True


bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)


remlist =[]


@bot.event
async def on_ready():
    await tree.sync()
    print("Ready!")

# guild=discord.Object(id=769145823119671316)

@tree.command(name = "hello", description = "greets with hello") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message(f"Hello! {interaction.user.mention}")


@tree.command(name = "add", description = "adds task")
async def addtolist(interaction):
    await add(interaction)

# bot = commands.Bot(command_prefix = '!', intents= intents)

# @bot.event
# async def on_ready():
#     print("Bot is up")
#     try:
#         synced = bot.tree.sync()
#         print(f"synced{len(synced)} commands")
#     except Exception as e:
#         print(e)


# @bot.command()
# async def  helpt(ctx):
#     await ctx.send(ctx.guild)
#     await ctx.send(ctx.author)
#     await ctx.send(ctx.message.id)
    

# @bot.tree.command(name = "about")
# async def about(interaction: discord.Interaction):
#     await interaction.response.send_message(f"Hey ! {interaction.user.mention}" , ephemeral = True)



bot.run(DISCORD_TOKEN)
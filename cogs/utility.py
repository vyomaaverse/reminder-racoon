import discord
from discord import client
import os
from discord.ext import commands


class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready!')
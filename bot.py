# bot.py
import os

import discord
from dotenv import load_dotenv


class MyClient(discord.Client):
    async def on_message(self, message):
        await message.channel.send('Hello World!')






# # id = 745059328674758688
# text: "745059329350172757"
# client = 751437378895347763
# load_dotenv()
# TOKEN = "NzUxNDM3Mzc4ODk1MzQ3NzYz.X1JEmA.vsQv47irDSyMFpk8ZyHRvKHzJiM"
# GUILD = "745059328674758688"
# channel = client.get_channel(text)
# await channel.send('hello')
# client = discord.Client()


# # client.run(TOKEN)


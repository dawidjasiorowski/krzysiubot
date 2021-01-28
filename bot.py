import discord
import os
import krzysiu

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith("#krzysiu"):
        await message.author.edit(nick=krzysiu.getName())
    if message.content.startswith("#powiedzenie"):
        await message.channel.send(krzysiu.getPhrase())
client.run(os.getenv("TOKEN"))

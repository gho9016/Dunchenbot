import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Dunchendiscordbot online")
    game = discord.Game("던첸봇일하는중...")
    await client.change_presence(status=discord.Status.online, activity=game)
@client.event
async def on_message(message):
    if message.content.startswith("!ping"):
        await message.channel.send("ping!")
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

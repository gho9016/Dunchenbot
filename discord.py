import discord
import os

client = discord.Client()

@client.event
async def on_redey():
    print("봇 시작")

    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

import discord, aiohttp, os
from discord.ext import commands

client = commands.Bot(command_prefix="f54f2163542a9d0df01264dfe", intents=discord.Intents().all(), activity=discord.Activity(type=discord.ActivityType.watching, name="emoji.instatus.com"))
BotWebhook = os.environ['BotWebhook']


@client.event
async def on_ready():
  print(f'Logged in as {client.user.name}#{client.user.discriminator} ({client.user.id})')
  
@client.event
async def on_member_update(before, after):
  if before.id == 882567620077957122 and before.status != after.status:
    if str(after.status) == 'offline':
      async with aiohttp.ClientSession() as session:
        async with session.post(BotWebhook, json={
        "trigger": "down",
        "name": "EmojiCord is offline",
        "message": "EmojiCord is offline unexpectedly. Please visit support server and let us know. discord.gg/NPxDRZGtvR",
        "status": "MAJOROUTAGE"
        }) as resp:
            print(resp)
    elif str(after.status) == 'online':
        async with aiohttp.ClientSession() as session:
            async with session.post(BotWebhook, json={
            "trigger": "up",
            "name": "EmojiCord is online",
            "message": "EmojiCord is back online.",
            "status": "OPERATIONAL"
            }) as resp:
                print(resp)

client.run(os.environ["TOKEN"])

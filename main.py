import schedule
import os
import discord

client= discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user} '.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!'):
    await message.channle.send('Event Will be created')

client.run(os.getenv('TOKEN'))

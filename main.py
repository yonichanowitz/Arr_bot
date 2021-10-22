import discord
import os
import requests
import json


my_secret = os.environ['bot_token']

# def get_quote():
#   response = requests.get('https://theysaidso.com/quotes/author/pirate-quote/')
#   json_data = json.loads(response.text)

client = discord.Client() 

@client.event
async def on_ready():
  print("🏴‍☠️ARRR! {0.user}".format(client))

@client.event
async def on_message(parrot):
  if parrot.author == client.user:
    return

  squawk = parrot.content

  if squawk.startswith('🏴‍☠️Ahoy!'):
    await parrot.channel.send('Ahoy Matey!')

  if squawk.startswith('🏴‍☠️Dict'):
    with open('pirateDictionary.json') as f:
      data = json.load(f)
      dictKeys = data.keys()
      if any(word in squawk for word in dictKeys):
        slicedStr = squawk[9:len(squawk)]
        await parrot.channel.send(data[slicedStr])
      else:
         await parrot.channel.send("'tis not a term me hearty!")
    

client.run(my_secret)


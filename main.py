from discord import Client, Intents
from random import choice
import os
import string
import metadata

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

feur_like = {
  "FEUR": "feur",
  "FEUR2": "FEUR !!!!!",
  "FEUR3": "quoicoubeh",
  "FEUR4": "feur je pense",
  "FEUR5": "COUBEEEEEEEEEEEEEEEEEEEH",
  "FEUR6": "et c'est le feur !",
  "FEUR7": "react"
}

pastabox = /stickers/{1120390316537675947}


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  message_test = message.content.lower().replace(" ", "").translate(
    str.maketrans('', '', string.punctuation))
  if message.author == client.user:
    return

  if (message_test.endswith('quoi') or message_test.endswith('quoient')
      or message_test.endswith('kwa') or message_test.endswith('kwoi')
      or message_test.endswith('kouaent') or message_test.endswith('qoua')
      or message_test.endswith('koua') or message_test.endswith('qwa')
      or message_test.endswith('koi')):
    feur = choice(list(feur_like.items()))
    if feur[1] != "react":
      await message.channel.send(f'{feur[1]}')
    else:
      await message.add_reaction('🇫')
      await message.add_reaction('🇪')
      await message.add_reaction('🇺')
      await message.add_reaction('🇷')

  if message_test.endswith('waf') or message_test.endswith('ouaf'):
    await message.channel.send('*pat pat*')

  if message.content == "!horny":
    await message.channel.send(choice(metadata.horny))

  if message.content == "!bonk":
    await message.channel.send(<:bonk:1103028667505979402>)

  if message.content == "!pastabox":
    await message.channel.send(pastabox)


if __name__ == "__main__":

  my_secret = os.environ['quoicoubot_id']
  client.run(my_secret)

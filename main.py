import discord
import requests
import keep_alive
import random
from datetime import datetime
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

DISCORD_KEY = environ.get("DISCORD_KEY")

client = discord.Client()
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '!newcode' in message.content[:8]:
      id = message.id
      user = message.author.name
      text = message.content[9:]
      time = message.created_at.strftime("%m/%d/%Y, %H:%M:%S")
      avatar = message.author.avatar
      userid = str(message.author.id)
      await message.channel.send(avatar + "gang" + userid)
      logInfo = {
            'id': id,
            'name': user,
            'text': text,
            'time': time,
            'pplink': 'https://cdn.discordapp.com/avatars/'+userid+'/'+avatar+'.jpg'
        }
      response = requests.post(f"https://CodeLogDiscordBot--sunghyounk.repl.co",data=logInfo)
      #raptor_link = response.json()["data"]["url"]
      #await message.channel.send(raptor_link)
        #aptor_img = requests.get(raptor_link)
        #poster = Image.open(BytesIO(raptor_img.content))
        #poster.save('Raptor.png','PNG')
        #file = discord.File('Raptor.png', filename='Raptor.png')
        #await message.channel.send(file=file)
        #os.remove("C:\\Users\\Sungh\\PycharmProjects\\Jewdah\\Raptor.png")

keep_alive.keep_alive()
client.run(DISCORD_KEY)
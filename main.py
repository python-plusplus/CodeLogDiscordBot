#h9lj35s8m6wnleNPYpiFm_kpF8QWtyDZ
import discord


client = discord.Client()
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '!' in message.content[:1]:
        if '!69.420xxxx' in message.content:
            await message.channel.send('Fuck you chubby')
        elif 'xx.xxxxxxx' in message.content:
            await message.channel.send('AHH SO CLOSE!!! Now remember what sunny first told you and apply it to the code.')
        else:
            await message.channel.send('')

import discord
import requests
import keep_alive
import random
boys = []
girls = []

client = discord.Client()
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '#spinthebottle' in message.content[:14]:
      boy = random.choice(boys)
      girl = random.choice(girls)
      await message.channel.send(boy + ' <3 ' + girl)
    if '#stb-list' in message.content[:9]:
      await message.channel.send(boys)
      await message.channel.send(girls)
    if '#stb-add-boy' in message.content[:12]:
      if message.content[13:] in boys:
        await message.channel.send('That person has already been added!')
      else:
        boys.append(message.content[13:])
        await message.channel.send(message.content[13:] + ' has been added to boys!')
    if '#stb-add-girl' in message.content[:13]:
      if message.content[14:] in boys:
        await message.channel.send('That person has already been added!')
      else:
        girls.append(message.content[14:])
        await message.channel.send(message.content[14:] + ' has been added to girls!')
    if '#stb-remove-boy' in message.content[:15]:
      boys.remove(message.content[13:])
    if '#stb-remove-girl' in message.content[:16]:
      girls.remove(message.content[14:])
    if '#RPT' in message.content:
        await message.channel.send("RPT " + message.content[5:])
        MEME_POST = {
            'template_id': 61516,
            'username': 'sunnyk',
            'password': 'Kissme77',
            'text0': 'RAPTOR PRO TIPS',
            'text1': message.content[5:]
        }
        response = requests.post(f"https://api.imgflip.com/caption_image",data=MEME_POST)
        raptor_link = response.json()["data"]["url"]
        await message.channel.send(raptor_link)
        #aptor_img = requests.get(raptor_link)
        #poster = Image.open(BytesIO(raptor_img.content))
        #poster.save('Raptor.png','PNG')
        #file = discord.File('Raptor.png', filename='Raptor.png')
        #await message.channel.send(file=file)
        #os.remove("C:\\Users\\Sungh\\PycharmProjects\\Jewdah\\Raptor.png")

keep_alive.keep_alive()
client.run("NjQyMjAwMTc5NzkyOTM2OTYw.XcTfHQ.k3jfJSRebIqUdJ50w3MqtaQEWZ4")
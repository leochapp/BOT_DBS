import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents, description="BOT Discord pour l'association Décibels")
intents.members = True
intents.message_content = True


@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user} ! ")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    words = message.content.lower().split()  # On prend les 10 premiers mots
    phrase = " ".join(words)  # On transforme les mots en une phrase

    if 'je suis' in phrase:
        try:
            index = words.index('je') + 1
            if words[index] == 'suis':
                # Récupérer le mot suivant et l'envoyer en réponse
                name = words[index+1:]
                t = ''
                for word in name:
                    t+= word +' '

                member = message.author
                await member.edit(nick=t)

                response = f'Le pseudo de {member.mention} vient dêtre modifié !'
                await message.channel.send(response)
        except:
            await message.channel.send(f"Bien esquivé  {member.mention}")


#Remplacez le TOKEN avec votre propre token de bot Discord
client.run(os.environ['TOKEN'])

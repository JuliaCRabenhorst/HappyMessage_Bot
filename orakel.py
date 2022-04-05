import os
import random
import discord


def aufruf(c, d):
    my_filey = open(c, d)
    contenty = my_filey.read()
    content_wort = contenty.split(",")
    my_filey.close()
    return content_wort


def make_text():
    content_smile = aufruf("D:/Program Files/ProgrammingStuff/Python/Python Stuff/Python Projekt/smiles.txt", "r")
    content_adj = aufruf("D:/Program Files/ProgrammingStuff/Python/Python Stuff/Python Projekt/adjectives.txt", "r")
    content_noun = aufruf("D:/Program Files/ProgrammingStuff/Python/Python Stuff/Python Projekt/nouns.txt", "r")
    a = len(content_adj) - 1
    b = len(content_noun) - 1
    c = len(content_smile) - 1
    n = random.randint(0, a)
    i = random.randint(0, b)
    e = random.randint(0, c)
    adj = content_adj[n]
    noun = content_noun[i]
    smile = content_smile[e]
    return "You are a" + adj + noun + smile


client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'Help!':
        response = 'Beep! = Boop \nBoop! or boop! = Happy Message \n'
        await message.channel.send(response)
    elif message.content == 'Beep!' or message.content == 'beep!':
        response = 'Boop!'
        await message.channel.send(response)
    elif message.content == 'Boop!' or message.content == 'boop!':
        response = make_text()
        await message.channel.send(response)


TOKEN = open("D:/Program Files/ProgrammingStuff/Python/Python Stuff/Python Projekt/TOKEN.txt", "r").readline()
client.run(TOKEN)

import discord
import config
import requests

client = discord.Client()

@client.event
async def on_ready():
    for guild_id in client.guilds:
        if guild_id.name == config.DISCORD_GUILD_NAME:
            break
        print(
            f'{client.user} is connected to {guild_id.name}(id: {guild_id.id})'
        )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    wordbank = ['cat', 'puppy', 'bunny', 'giraffe', 'poop']

    if message.content == 'pycascade':
        response = 'Hello everyone! Welcome and have a great time!'
        await message.channel.send(response)
    elif message.content in wordbank:
        await message.channel.send("please don't use bad words")
    elif 'pokemon' in message.content:
        # input: pokemon pikachu
        pokemon = message.content.split()[1]
        req = requests.get(f"https://getpokemonweakness.azurewebsites.net/api/getweakness?pokemon={pokemon}")
        await message.channel.send(req.content)
client.run(config.DISCORD_BOT_TOKEN)
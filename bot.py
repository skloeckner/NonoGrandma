import discord
import random
import os

from utils import load_phrases

client = discord.Client()

phrases = load_phrases(os.path.join(os.getcwd(), 'data', 'phrases.txt'))

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # List of curse words to check against
    curse_words = ['heck', 'darn', 'blast', 'gosh']

    # Check if message contains a curse word
    for word in curse_words:
        if word in message.content.lower():
            # Send scolding message with a random phrase
            phrase = random.choice(phrases)
            await message.channel.send(f"Oh my goodness, {message.author.mention}! {phrase} Please watch your language and refrain from using such naughty words like '{word}'!")

client.run('YOUR_DISCORD_BOT_TOKEN')

import discord
import random

# Define the list of curse words to check against
CURSE_WORDS = ['fuck', 'shit', 'bitch', 'asshole', 'dick', 'pussy', 'cock', 'cunt', 'motherfucker', 'twat', 'bastard', 'damn', 'hell', 'fag', 'nigga', 'slut', 'whore']

# Define the list of scolding phrases
PHRASES = [
    "Now now, watch your language young one!",
    "In my day, we didn't use language like that!",
    "Such foul language, young people these days...",
    "There's no need for that kind of language!",
    "Please refrain from using that kind of language in this server!",
    "I'm going to have to wash your mouth out with soap if you keep that up!",
    "That kind of language is not acceptable!",
    "This is a family-friendly server, please keep your language appropriate!",
    "Language like that will not be tolerated here!",
    "Do you kiss your mother with that mouth?",
    "That kind of language is a no-no!",
    "Watch your mouth, young one!",
    "No cursing allowed in this server!"
]

# Define the Discord client
client = discord.Client()

# Define the on_ready event handler
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Define the on_message event handler
@client.event
async def on_message(message):
    # Ignore messages from the bot itself to avoid infinite loops
    if message.author == client.user:
        return

    # Check if the message contains a curse word
    if any(word in message.content.lower() for word in CURSE_WORDS):
        # Choose a random scolding phrase and send it as a message
        await message.channel.send(random.choice(PHRASES))

# Run the bot using the provided API key
client.run('YOUR_DISCORD_API_KEY_HERE')

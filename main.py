import discord
from discord.ext import commands
from discord import app_commands
import json
import random

# Load the quotes from the JSON file
with open('quotes.json') as f:
    quotes_data = json.load(f)
quotes = quotes_data['quotes']

# Load the gifs from the JSON file
with open('gifs.json') as f:
    gifs_data = json.load(f)
gifs = gifs_data['gifs']

# Set up the bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

# Load the token from the environment variable
token = 'DISCORD_BOT_TOKEN'

# TempleOS teal color for footers
TEMPLEOS_COLOR = 0x008080

# Event listener for when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# Hybrid command to get information about Terry Davis
@bot.hybrid_command(name='terry', description='Get information about Terry Davis')
async def terry(ctx):
    embed = discord.Embed(description="Terry Davis was the creator of TempleOS, a unique operating system he developed over a decade. He was a brilliant programmer and a fascinating individual with a complex personal life.", color=TEMPLEOS_COLOR)
    embed.set_footer(text="Terry Davis Info")
    await ctx.send(embed=embed)

# Hybrid command to get information about TempleOS
@bot.hybrid_command(name='templeos', description='Learn about the TempleOS operating system')
async def templeos(ctx):
    embed = discord.Embed(description="TempleOS is a unique operating system developed by Terry Davis over the course of a decade. It features a custom programming language, a unique 3D metaphor, and a focus on religious themes. Despite its unconventional nature, TempleOS has gained a cult following among programmers and enthusiasts.", color=TEMPLEOS_COLOR)
    embed.set_footer(text="TempleOS Info")
    await ctx.send(embed=embed)

# Hybrid command to get a random quote from Terry Davis
@bot.hybrid_command(name='quote', description='Get a random quote from Terry Davis')
async def quote(ctx):
    quote = random.choice(quotes)
    embed = discord.Embed(description=f"*{quote}* - Terry Davis", color=TEMPLEOS_COLOR)
    embed.set_footer(text="Random Terry Davis Quote")
    await ctx.send(embed=embed)

# Hybrid command to get links to relevant resources
@bot.hybrid_command(name='resources', description='Get links to relevant resources and documentation')
async def resources(ctx):
    embed = discord.Embed(description="**Here are some relevant resources:**\n\nTempleOS website: <https://templeos.org>\nTerry Davis documentary: <https://www.youtube.com/watch?v=UCgoxQCf5Jg&pp=ygUXdGVycnkgZGF2aXMgZG9jdW1lbnRhcnk%3D>\nTempleOS GitHub repository: <https://github.com/cia-foundation/TempleOS>\nTerry Davis Wikipedia page: <https://en.wikipedia.org/wiki/Terry_A._Davis>", color=TEMPLEOS_COLOR)
    embed.set_footer(text="Relevant Resources")
    await ctx.send(embed=embed)

# Hybrid command to get a random gif
@bot.hybrid_command(name='gif', description='Get a random gif')
async def gif(ctx):
    # Calculate the total probability
    total_probability = sum(gif['probability'] for gif in gifs)

    # Generate a random number between 0 and the total probability
    random_number = random.uniform(0, total_probability)

    # Iterate through the gifs and select the first one with a probability range that includes the random number
    current_probability = 0
    selected_gif = None
    for gif in gifs:
        current_probability += gif['probability']
        if random_number < current_probability:
            selected_gif = gif
            break

    # Send the selected gif
    if selected_gif:
        await ctx.send(selected_gif['url'])
    else:
        await ctx.send('No gifs found.')

# Hybrid command to display available commands
@bot.hybrid_command(name='help', description='List available commands')
async def help(ctx):
    embed = discord.Embed(title="Available Commands", color=TEMPLEOS_COLOR)
    
    embed.add_field(name="Information", value="!terry: Get biographical information about Terry Davis.\n!templeos: Learn about the TempleOS operating system.", inline=False)
    embed.add_field(name="Quotes", value="!quote: Receive an interesting fact or quote about Terry Davis or TempleOS.", inline=False)
    embed.add_field(name="Resources", value="!resources: Get links to relevant resources and documentation.", inline=False)
    embed.add_field(name="Fun", value="!gif: Generate a random Terry Davis or TempleOS-related gif.", inline=False)
    embed.add_field(name="Utility", value="!help: Displays this help message.\n!ping: Check the bot's latency.", inline=False)

    embed.set_footer(text="TempleOS Bot Help")
    await ctx.send(embed=embed)

# Hybrid command to check the bot's latency
@bot.hybrid_command(name='ping', description='Check the bot\'s latency')
async def ping(ctx):
    embed = discord.Embed(description=f'Pong! Latency: {round(bot.latency * 1000)}ms', color=TEMPLEOS_COLOR)
    embed.set_footer(text="Bot Latency")
    await ctx.send(embed=embed)

# Start the bot
bot.run(token)
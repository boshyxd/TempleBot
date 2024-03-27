import discord
from discord.ext import commands

# Set up the bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

# Load the token from the environment variable
token = 'DISCORD_BOT_TOKEN'

# Event listener for when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Example command to get information about Terry Davis
@bot.command()
async def terry(ctx):
    await ctx.send("Terry Davis was the creator of TempleOS, a unique operating system he developed over a decade. He was a brilliant programmer and a fascinating individual with a complex personal life.")

# Start the bot
bot.run(token)
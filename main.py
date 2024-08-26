import discord
from discord.ext import commands
import json
import random
import os
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# Load environment variables
load_dotenv()

# Get the token
token = os.getenv('DISCORD_BOT_TOKEN')

if not token:
    raise ValueError("DISCORD_BOT_TOKEN not found in environment variables")

# Load quotes and gifs
with open('quotes.json') as f:
    quotes = json.load(f)['quotes']

with open('gifs.json') as f:
    gifs = json.load(f)['gifs']

# Set up the bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

TEMPLEOS_COLOR = 0x008080

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.tree.sync()

@bot.hybrid_command(name='terry', description='Get information about Terry Davis')
async def terry(ctx):
    embed = discord.Embed(description="Terry Davis was the creator of TempleOS, a unique operating system he developed over a decade.", color=TEMPLEOS_COLOR)
    await ctx.send(embed=embed)

@bot.hybrid_command(name='templeos', description='Learn about the TempleOS operating system')
async def templeos(ctx):
    embed = discord.Embed(description="TempleOS is a unique operating system developed by Terry Davis, featuring a custom programming language and 3D metaphor.", color=TEMPLEOS_COLOR)
    await ctx.send(embed=embed)

@bot.hybrid_command(name='quote', description='Get a random quote from Terry Davis')
async def quote(ctx):
    embed = discord.Embed(description=f"*{random.choice(quotes)}* - Terry Davis", color=TEMPLEOS_COLOR)
    await ctx.send(embed=embed)

@bot.hybrid_command(name='resources', description='Get links to relevant resources and documentation')
async def resources(ctx):
    resources_text = "**Relevant resources:**\n\nTempleOS website: <https://templeos.org>\nTerry Davis documentary: <https://www.youtube.com/watch?v=UCgoxQCf5Jg>\nTempleOS GitHub: <https://github.com/cia-foundation/TempleOS>\nTerry Davis Wikipedia: <https://en.wikipedia.org/wiki/Terry_A._Davis>"
    embed = discord.Embed(description=resources_text, color=TEMPLEOS_COLOR)
    await ctx.send(embed=embed)

@bot.hybrid_command(name='gif', description='Get a random gif')
async def gif(ctx):
    total_probability = sum(gif['probability'] for gif in gifs)
    random_number = random.uniform(0, total_probability)
    
    current_probability = 0
    for gif in gifs:
        current_probability += gif['probability']
        if random_number < current_probability:
            await ctx.send(gif['url'])
            return
    
    await ctx.send('No gifs found.')

def create_color_image(colors):
    width, height = 800, 600
    image = Image.new('RGBA', (width, height), color=(0,0,0,0))  # Transparent background
    draw = ImageDraw.Draw(image)
    
    # Use a system font
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except IOError:
        font = ImageFont.load_default()

    square_size = 120
    padding = 20
    cols = 4
    rows = 4

    for i, (color_hex, color_name) in enumerate(colors):
        row = i // cols
        col = i % cols
        x = col * (square_size + padding) + padding
        y = row * (square_size + padding) + padding

        # Draw color square with rounded corners
        draw.rounded_rectangle([x, y, x + square_size, y + square_size], radius=10, fill=f'#{color_hex:06x}')
        
        # Draw color name
        text_color = 'white' if color_hex < 0x808080 else 'black'
        text_bbox = draw.textbbox((0, 0), color_name, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = x + (square_size - text_width) / 2
        text_y = y + square_size - text_height - 10
        draw.text((text_x, text_y), color_name, font=font, fill=text_color)

    buffer = BytesIO()
    image.save(buffer, 'PNG')
    buffer.seek(0)
    return buffer

@bot.hybrid_command(name='colors', description='Show TempleOS color scheme')
async def colors(ctx):
    colors = [
        (0x000000, "Black"), (0x0000AA, "Blue"), (0x00AA00, "Green"), (0x00AAAA, "Cyan"),
        (0xAA0000, "Red"), (0xAA00AA, "Magenta"), (0xAA5500, "Brown"), (0xAAAAAA, "Light Gray"),
        (0x555555, "Dark Gray"), (0x5555FF, "Light Blue"), (0x55FF55, "Light Green"), (0x55FFFF, "Light Cyan"),
        (0xFF5555, "Light Red"), (0xFF55FF, "Light Magenta"), (0xFFFF55, "Yellow"), (0xFFFFFF, "White")
    ]
    
    color_image = create_color_image(colors)
    file = discord.File(color_image, filename="templeos_colors.png")
    
    embed = discord.Embed(title="TempleOS Color Scheme", color=TEMPLEOS_COLOR)
    embed.set_image(url="attachment://templeos_colors.png")
    embed.set_footer(text="TempleOS uses a 16-color palette")
    
    await ctx.send(file=file, embed=embed)

@bot.hybrid_command(name='help', description='List available commands')
async def help(ctx):
    commands_list = [
        ("Information", "!terry, !templeos"),
        ("Quotes", "!quote"),
        ("Resources", "!resources"),
        ("Fun", "!gif"),
        ("Utility", "!help, !ping"),
        ("Colors", "!colors")
    ]
    
    embed = discord.Embed(title="Available Commands", color=TEMPLEOS_COLOR)
    for category, cmds in commands_list:
        embed.add_field(name=category, value=cmds, inline=False)
    
    await ctx.send(embed=embed)

@bot.hybrid_command(name='ping', description='Check the bot\'s latency')
async def ping(ctx):
    embed = discord.Embed(description=f'Pong! Latency: {round(bot.latency * 1000)}ms', color=TEMPLEOS_COLOR)
    await ctx.send(embed=embed)

# Start the bot
bot.run(token)
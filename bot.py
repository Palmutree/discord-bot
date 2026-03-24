import os
import discord
from discord.ext import commands
from env import DISCORD_TOKEN, load_env
from aiohttp import web
import asyncio

# Load the bot token from the env file
load_env()

# Define the bot's prefix and intents (adjust intents as needed)
intents = discord.Intents.default()
intents.message_content = True # Enable message content intent for reading messages
intents.members = True # Enable members intent to detect joins
bot = commands.Bot(command_prefix='!', intents=intents)

# Simple web server to keep bot alive
async def handle_ping(request):
    return web.Response(text="Bot is alive!")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()
    print("Web server started on port 8080")

# Event: Bot is ready and online
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!') #
    # Start web server when bot connects
    if not hasattr(bot, 'web_server_started'):
        await start_web_server()
        bot.web_server_started = True

# Event: A new member joins the server
@bot.event
async def on_member_join(member):
    # Replace '12485148156646654062' with your actual channel ID
    channel = bot.get_channel(1485148156646654062)
    if channel is not None:
        embed = discord.Embed(
            title="⌗ welcome┆★ ₊ ˚⟡",
            description=f"hey {member.mention} ",
            color=discord.Color.from_str("#171717")
        )
        await channel.send(embed=embed)

# Command: A simple ping command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!') #

# Run the bot
bot.run(DISCORD_TOKEN)

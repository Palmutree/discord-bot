import os
import discord
from discord.ext import commands
from env import DISCORD_TOKEN, load_env
from aiohttp import web
import asyncio

load_env()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix='!', intents=intents)

async def handle_ping(request):
    return web.Response(text="Bot is alive!")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get('PORT', 5000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Web server started on port {port}")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(status=discord.Status.online)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1485148156646654062)
    if channel is not None:
        embed = discord.Embed(
            title="⌗ welcome┆★ ₊ ˚⟡",
            description=f"hey {member.mention} ",
            color=discord.Color.from_str("#171717")
        )
        await channel.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

async def main():
    await start_web_server()
    await bot.start(DISCORD_TOKEN)

asyncio.run(main())

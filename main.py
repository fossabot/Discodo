import discord
from discord.ext import commands
import logging, asyncio, os, json

loop = asyncio.get_event_loop

def get_setting() -> dict:
    with open('settings.json', 'r', encoding="UTF-8") as f:
        return json.load(f)

logger = logging.getLogger('discord')
logging.basicConfig(level=logging.INFO)
handler = logging.FileHandler(filename=f'logging.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix="!", help_command=None)
TOKEN = "enable_token"

@bot.event
async def on_connect():
    print("Bot connect!")

@bot.event
async def on_disconnect():
    print("Bot disconnect!")

@bot.event
async def on_ready():
    logger.info(f"{bot.user.name} | {bot.user.id}")

@bot.event
async def on_message(message):
    if message.author.bot and not message.guild:
        return
    
    await bot.process_commands(message)

[bot.load_extension(f"command.{x.replace('.py', '')}") for x in os.listdir("./command") if x.endswith('.py')]

bot.run(get_setting()[TOKEN], bot=True, reconnect=True)
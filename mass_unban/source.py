import discord
import asyncio
import colorama
from colorama import Fore, Style
from discord.ext import commands

colorama.init()

intents = discord.Intents.default()
intents.bans = True

bot = commands.Bot(command_prefix='.', intents=intents ,self_bot = True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (cmd = .unbanall)')

@bot.command()
async def unbanall(ctx):
    banned_users = await ctx.guild.bans()
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    for index, ban_entry in enumerate(banned_users):
        user = ban_entry.user
        color = colors[index % len(colors)]
        await asyncio.sleep(1)  # dont change this or else you will get rate limted
        await ctx.guild.unban(user)
        print(f'{color}Unbanned {user.name} ({user.id}){Style.RESET_ALL}')

def get_bot_token():
    return input("Enter your user token: ")

bot_token = get_bot_token()
bot.run(bot_token ,bot = False)

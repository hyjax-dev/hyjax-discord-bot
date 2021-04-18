# bot.py
import os
import random
import discord
import time

from discord.ext import commands
from dotenv import load_dotenv

# importing your Discord Token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# create bot var and prefix
bot = commands.Bot(command_prefix='h!')




@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('Du hast die benötigten Rechte nicht!')

@bot.command(name='69', help='Just nice!')
async def six_nine(ctx):
    await ctx.send('nice!')

@bot.command(name='roll_dice', help='(würfel, augen) simuliert einen würfel')
async def roll_dice(ctx, number_of_dices, number_of_sides):
    dice = [
        str(random.choice(range(1, number_of_sides)))
        for _ in range(number_of_dices)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='create-voice', help='Erstellt einen Voice channel')
@commands.has_role('Admin')
async def create_channel(ctx, channel_name="Default Channel"):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Erstelle den Spach-channel "{channel_name}"')
        await guild.create_voice_channel(channel_name)

if __name__ == "__main__":
    bot.run(TOKEN)
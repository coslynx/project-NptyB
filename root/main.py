# main.py (Python)

import discord
from discord.ext import commands
import asyncio
import logging

from config import settings
from moderation import filter
from moderation import warning
from moderation import action
from interface import dashboard
from logs import moderation_logs

# Initialize the Discord bot
bot = commands.Bot(command_prefix='!')

# Event for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Event for filtering inappropriate content
@bot.event
async def on_message(message):
    if filter.filter_content(message):
        await message.delete()
        await message.channel.send(f'{message.author.mention}, please refrain from using inappropriate language.')
        warning.add_warning(message.author)
        if warning.get_warnings(message.author) == settings.MAX_WARNINGS:
            action.ban_user(message.author)
        elif warning.get_warnings(message.author) >= settings.WARNINGS_THRESHOLD:
            action.mute_user(message.author)

# Command to display the moderation dashboard
@bot.command(name='dashboard')
async def display_dashboard(ctx):
    await ctx.send(embed=dashboard.generate_dashboard())

# Start the bot
bot.run(settings.TOKEN)
# dashboard.py (Python)

import discord
from discord.ext import commands
from moderation.filter import automatic_filter
from moderation.warning import warning_system
from moderation.action import perform_action
from config.settings import custom_settings

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Automatic content filtering
    if automatic_filter(message.content):
        await message.delete()
        await message.channel.send(f'{message.author.mention}, please refrain from using inappropriate language.')

    await bot.process_commands(message)

@bot.command()
async def warn(ctx, user: discord.Member, reason):
    # Warning system implementation
    if warning_system(user):
        await ctx.send(f'{user.mention} has been warned for: {reason}')
    else:
        await ctx.send(f'Unable to warn {user.mention}. Please try again later.')

@bot.command()
async def mute(ctx, user: discord.Member):
    # Mute user action
    if perform_action('mute', user):
        await ctx.send(f'{user.mention} has been muted.')
    else:
        await ctx.send(f'Unable to mute {user.mention}. Please try again later.')

@bot.command()
async def ban(ctx, user: discord.Member):
    # Ban user action
    if perform_action('ban', user):
        await ctx.send(f'{user.mention} has been banned.')
    else:
        await ctx.send(f'Unable to ban {user.mention}. Please try again later.')

# Customizable settings for moderation
@bot.command()
async def set_settings(ctx, **kwargs):
    custom_settings.update(kwargs)
    await ctx.send('Settings updated successfully.')

# User-friendly interface for server management
@bot.command()
async def server_info(ctx):
    server = ctx.guild
    embed = discord.Embed(title="Server Information", description=f"Here is some information about {server.name}",
                          color=discord.Color.blue())
    embed.add_field(name="Server ID", value=server.id, inline=False)
    embed.add_field(name="Total Members", value=server.member_count, inline=False)
    embed.add_field(name="Server Owner", value=server.owner, inline=False)
    await ctx.send(embed=embed)

bot.run('YOUR_DISCORD_BOT_TOKEN')
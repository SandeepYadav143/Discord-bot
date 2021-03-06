import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
from pretty_help import PrettyHelp # pip install discord-pretty-help

intents = discord.Intents.default()
intents.members = True

prefix_list = ["K.", "k.", "kanao ", "kanao", "Kanao ", "Kanao"]
bot = commands.Bot(
    command_prefix = prefix_list,
    case_insensitive = True,
    strip_after_prefix = True,
    intents = intents,
    description = "Still Development."
    # help_command = PrettyHelp()
    )

@bot.command(hidden = True)
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"commands.{extension}")
    await ctx.send(f"✅ Successfully loaded {extension} cog.")

@load.error
async def load_error(ctx, error):
    await ctx.send(error)

@bot.command(hidden = True)
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"commands.{extension}")
    await ctx.send(f"✅ Successfully unloaded {extension} cog.")

@unload.error
async def unload_error(ctx, error):
    await ctx.send(error)

@bot.command(hidden = True)
@commands.is_owner()
async def reload(ctx, extension):
    bot.unload_extension(f"commands.{extension}")
    await ctx.send(f"✅ Successfully unloaded {extension} cog.")
    
    bot.load_extension(f"commands.{extension}")
    await ctx.send(f"✅ Successfully loaded {extension} cog.
    ")

@reload.error
async def reload_error(ctx, error):
    await ctx.send(error)


for filename in os.listdir("./commands"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"commands.{filename[:-3]}")


keep_alive()
bot.run(os.getenv("TOKEN"))
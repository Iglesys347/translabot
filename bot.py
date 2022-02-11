import discord
from discord.ext import commands
from matplotlib.image import thumbnail
from tabulate import tabulate
from deep_translator import GoogleTranslator

from message_parser import MessageParser


TARGET_LANGUAGE = "en"
SOURCE_LANGUAGE = "auto"

bot = commands.Bot(command_prefix='!')
translator = GoogleTranslator


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def languages(ctx):
    embed = discord.Embed(title="Supported languages", url="https://github.com/Iglesys347/translabot#supported-languages",
                          description="Non-exhaustive list of supported languages depending on the translator used.",
                          color=discord.Color.blurple())
    await ctx.send("Here you can find a list of the currently supported languages :")
    await ctx.send(embed=embed)


@bot.command()
async def translate(ctx,  *, text):
    target = TARGET_LANGUAGE
    source = SOURCE_LANGUAGE
    mp = MessageParser(text)
    message, args = mp.parse()
    if "target" in args.keys():
        if args["target"] in translator.get_supported_languages():
            target = args["target"]
    if "source" in args.keys():
        if args["source"] in translator.get_supported_languages():
            source = args["source"]

    translated = translator(source=source, target=target).translate(
        text=message)
    await ctx.send(translated)

with open(".token") as f:
    token = f.read()

bot.run(token)

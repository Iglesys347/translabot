import discord
from discord.ext import commands
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
    langs = translator.get_supported_languages()
    await ctx.send(f"Here are the supported languages: {', '.join(langs)}.")


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

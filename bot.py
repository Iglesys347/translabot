from message_parser import MessageParser
import discord
from discord.ext import commands
import deep_translator
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

conf = dict(os.environ)

TOKEN = conf["TOKEN"]
TARGET_LANGUAGE = conf["TARGET"]
SOURCE_LANGUAGE = conf["SOURCE"]
TRANSLATOR_NAME = conf["TRANSLATOR"]
KEY = conf["KEY"]

DEFAULT_CONFIG = {
    "src": "auto",
    "tgt": "english",
    "translator": deep_translator.GoogleTranslator,
    "translator_name": "Google"
}

TRANSLATORS = {
    "Google": {
        "translator": deep_translator.GoogleTranslator,
        "key_needed": False
    },
    "Mymemory": {
        "translator": deep_translator.MyMemoryTranslator,
        "key_needed": False
    },
    "DeepL": {
        "translator": deep_translator.DeepL,
        "key_needed": True
    },
    "Microsoft": {
        "translator": deep_translator.MicrosoftTranslator,
        "key_needed": True
    },
    "Libre": {
        "translator": deep_translator.LibreTranslator,
        "key_needed": False
    }
}

bot = commands.Bot(command_prefix='!')
try:
    TRANSLATOR = TRANSLATORS[TRANSLATOR_NAME]["translator"]
    if TRANSLATORS[TRANSLATOR_NAME]["key_needed"]:
        TRANSLATOR = TRANSLATOR(api_key=KEY)
except KeyError:
    logger.error(
        "The translator %s does not match any known transaltor names.", TRANSLATOR_NAME)
    logger.info("Using default translator : %s", DEFAULT_CONFIG["translator"])
    TRANSLATOR = DEFAULT_CONFIG["translator"]
    TRANSLATOR_NAME = DEFAULT_CONFIG["translator_name"]


@bot.command()
async def languages(ctx, translator=None):
    if translator:
        if translator in TRANSLATORS.keys():
            await ctx.send(f"The supported languages for the translator {translator} are the following : {', '.join(TRANSLATOR.get_supported_languages())}.")
        else:
            await ctx.send(f"The translator name given does not match supported translators. The supported transaltors are : ")
    else:
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
        if args["target"] in TRANSLATOR.get_supported_languages():
            target = args["target"]
    if "source" in args.keys():
        if args["source"] in TRANSLATOR.get_supported_languages():
            source = args["source"]

    translated = TRANSLATOR(source=source, target=target).translate(
        text=message)
    await ctx.send(translated)


@bot.command()
async def target_language(ctx, target_language=None):
    global TARGET_LANGUAGE
    global TRANSLATOR
    if target_language:
        if target_language in TRANSLATOR.get_supported_languages():
            TARGET_LANGUAGE = target_language
            await ctx.send(f"Successfully changed target language to **{target_language}**.")
        else:
            await ctx.send(f"The language {target_language} is not supported by the translator. To see the supported languages by your current translator, please use the command `!languages {TRANSLATOR_NAME}`.")
    else:
        await ctx.send(f"The current target language is **{TARGET_LANGUAGE}**. To change it, you can use the command `!target_language language` (e.g. `!target_language french`).")


@bot.command()
async def source_language(ctx, source_language=None):
    global SOURCE_LANGUAGE
    global TRANSLATOR
    if source_language:
        if source_language in TRANSLATOR.get_supported_languages():
            SOURCE_LANGUAGE = source_language
            await ctx.send(f"Successfully changed source language to **{source_language}**.")
        else:
            await ctx.send(f"The language {source_language} is not supported by the translator. To see the supported languages by your current translator, please use the command `!languages {TRANSLATOR_NAME}`.")
    else:
        await ctx.send(f"The current target language is **{SOURCE_LANGUAGE}**. To change it, you can use the command `!source_language language` (e.g. `!source_language french`). You can set it to 'auto' to let the translator automatically recognize the source language.")


@bot.command()
async def translator(ctx, translator=None):
    global TRANSLATOR_NAME, TRANSLATOR
    if translator:
        if translator in TRANSLATORS.keys():
            TRANSLATOR_NAME = translator
            TRANSLATOR = TRANSLATORS[translator]["translator"]
            await ctx.send(f"Successfully changed translator to **{TRANSLATOR_NAME}**.")
        else:
            await ctx.send(f"The translator {translator} is not supported. The supported translators are the following :     {', '.join(TRANSLATORS.keys())}.")
    else:
        await ctx.send(f"The current translator is **{TRANSLATOR_NAME}**. To change it, you can use the command `!translator translator_name` (e.g. `!translator Google`).")


bot.run(TOKEN)

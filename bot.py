"""
Module containing the main code for the bot.

Bot commands :
- languages : give the supported languages,
- transalte : translate the given text,
- target_language : change the default target language or display the current one,
- source_language : change the default source language or display the current one,
- translator : change the default translator or display the current one.
"""

import json
import logging
import discord
from discord.ext import commands
import deep_translator

from message_parser import MessageParser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

with open("conf.json", "r", encoding="utf_8") as conf_file:
    conf = json.load(conf_file)

TGT_LANGUAGE = conf["tgt"]
SRC_LANGUAGE = conf["src"]
TRANSLATOR_NAME = conf["translator_name"]

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
    TRANSL = TRANSLATORS[TRANSLATOR_NAME]["translator"]
    if TRANSLATORS[TRANSLATOR_NAME]["key_needed"]:
        TRANSL = TRANSL(api_key=conf["key"])
except KeyError:
    logger.error(
        "The translator %s does not match any known transaltor names.", TRANSLATOR_NAME)
    logger.info("Using default translator : %s", DEFAULT_CONFIG["translator"])
    TRANSL = DEFAULT_CONFIG["translator"]
    TRANSLATOR_NAME = DEFAULT_CONFIG["translator_name"]


@bot.command()
async def languages(ctx, _translator=None):
    """
    Show the supported languages, or a link to a file describing the supported languages.

    Parameters
    ----------
    translator : str, default='None'
        The translator name.

    Examples
    --------
    Bot command examples :
        !languages : send a link to a page referencing the supported languages.
        !languages <translator_name> : show the languages supported by the translator.

    See also
    --------
    List the supported languages : https://github.com/Iglesys347/translabot#supported-languages
    """
    if _translator:
        if _translator in TRANSLATORS:
            await ctx.send(f"The supported languages for the translator {_translator} "
                           "are the following: "
                           f"{', '.join(TRANSL.get_supported_languages())}.")
        else:
            await ctx.send("The translator name given does not match supported translators. "
                           f"The supported transaltors are: {', '.join(TRANSLATORS)}")
    else:
        embed = discord.Embed(
            title="Supported languages",
            url="https://github.com/Iglesys347/translabot#supported-languages",
            description="Non-exhaustive list of supported languages depending\
                on the translator used.",
            color=discord.Color.blurple())
        await ctx.send("Here you can find a list of the currently supported languages :")
        await ctx.send(embed=embed)


@bot.command()
async def translate(ctx, *, text=None):
    """
    Translate the text.

    Parameters
    ----------
    text : str, default=None
        The text to translate and the possible arguments. Arguments must be preceded by - or --.
        The possible arguments are :
            source, src, s : the source language to translate from
            target, tgt, t : the target language to translate

    Examples
    --------
    Bot command examples :
        `!translate <text to transalte>` : translate the given text into the configured
        language (default is english).
        `!translate --target=french <text to translate>` : translate the given text
        into the target language (here french). You can also use the following abbreviations :
        `-tgt`, `-t`.
        `!translate --source=french <text to transalte>` : translate the given text from
        the specified language (here french). You can also use the following abbreviations :
        `-src`, `-s`.

    See also
    --------
    List the supported languages : https://github.com/Iglesys347/translabot#supported-languages
    """
    target = TGT_LANGUAGE
    source = SRC_LANGUAGE
    if text is None:
        await ctx.send("There is nothing to translate :confused:")
    else:
        mess_parser = MessageParser(text)
        message, args = mess_parser.parse()
        if "target" in args:
            if args["target"] in TRANSL.get_supported_languages():
                target = args["target"]
        if "source" in args:
            if args["source"] in TRANSL.get_supported_languages():
                source = args["source"]

        translated = TRANSL(source=source, target=target).translate(
            text=message)
        await ctx.send(translated)


@bot.command()
async def target_language(ctx, _target_language=None):
    """
    Change the default target language or give the current one if no parameter is passed.

    Parameters
    ----------
    target_language : str, default=None
        The new default target language.

    Examples
    --------
    Bot command examples :
        `!target_language` : give the current default target language.
        `!target_language french` : change the default target language to french.

    See also
    --------
    List the supported languages : https://github.com/Iglesys347/translabot#supported-languages
    """
    global TGT_LANGUAGE
    if _target_language:
        if _target_language in TRANSL.get_supported_languages():
            TGT_LANGUAGE = _target_language
            await ctx.send(f"Successfully changed target language to **{_target_language}**.")
        else:
            await ctx.send(f"The language {_target_language} is not supported by the translator. "
                           "To see the supported languages by your current translator, please use "
                           f"the command `!languages {TRANSLATOR_NAME}`.")
    else:
        await ctx.send(f"The current target language is **{TGT_LANGUAGE}**. "
                       "To change it, you can use the command `!target_language <language>` "
                       "(e.g. `!target_language french`).")


@bot.command()
async def source_language(ctx, _source_language=None):
    """
    Change the default source language or give the current one if no parameter is passed.

    Parameters
    ----------
    source_language : str, default=None
        The new default source language.

    Examples
    --------
    Bot command examples :
        `!source_language` : give the current default source language.
        `!source_language french` : change the default source language to french.

    See also
    --------
    List the supported languages : https://github.com/Iglesys347/translabot#supported-languages
    """
    global SRC_LANGUAGE
    if _source_language:
        if _source_language in TRANSL.get_supported_languages():
            SRC_LANGUAGE = _source_language
            await ctx.send(f"Successfully changed source language to **{_source_language}**.")
        else:
            await ctx.send(f"The language {_source_language} is not supported by the translator. "
                           "To see the supported languages by your current translator, please use "
                           f"the command `!languages {TRANSLATOR_NAME}`.")
    else:
        await ctx.send(f"The current target language is **{SRC_LANGUAGE}**. "
                       "To change it, you can use the command `!source_language <language>` "
                       "(e.g. `!source_language french`). You can set it to 'auto' to "
                       "let the translator automatically recognize the source language.")


@bot.command()
async def translator(ctx, _translator=None):
    """
    Change the default  translator or give the current one if no parameter is passed.

    Parameters
    ----------
    translator : str, default=None
        The new default translator language.

    Examples
    --------
    Bot command examples :
        `!translator` : give the current default translator.
        `!translator Google` : change the default translator to Google.

    See also
    --------
    List the supported languages : https://github.com/Iglesys347/translabot#supported-languages
    """
    global TRANSLATOR_NAME, TRANSL
    if _translator:
        if _translator in TRANSLATORS:
            TRANSLATOR_NAME = _translator
            TRANSL = TRANSLATORS[_translator]["translator"]
            await ctx.send(f"Successfully changed translator to **{TRANSLATOR_NAME}**.")
        else:
            await ctx.send(f"The translator {_translator} is not supported. "
                           "The supported translators are the following : "
                           f"{', '.join(TRANSLATORS.keys())}.")
    else:
        await ctx.send(f"The current translator is **{TRANSLATOR_NAME}**. "
                       "To change it, you can use the command `!translator <translator_name>` "
                       "(e.g. `!translator Google`).")


bot.run(conf["bot_token"])

# Translabot

Discord bot for message translation in different languages.

![Bot image](ressources/translabot_white.png)

## Supported languages

The languages supported depend on the type of translator used. The available translators are some of the ones implemented in [deep-transaltor repo](https://github.com/nidhaloff/deep-translator):

- [Google Translate](https://translate.google.com)
- [Mymemory](https://mymemory.translated.net)
- [DeepL](https://www.deepl.com/translator) (API key needed)
- [Microsoft Translator](https://www.microsoft.com/translator/) (API key needed)
- [Libre Translate](https://libretranslate.com/)

The basic configuration uses the Google Translate translator.

Here is a summary table of the languages supported by each translator:

|           Language            |       Google       |      Mymemory      |       Deepl        |     Microsoft      |       Libre        |
| :---------------------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: |
|           afrikaans           | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|           albanian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            amharic            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            arabic             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
|           armenian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|           assamese            |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |
|          azerbaijani          | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            bashkir            |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |
|            basque             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|          belarusian           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|            bengali            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            bosnian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|           bulgarian           | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|            burmese            |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |
|            catalan            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            cebuano            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|           chichewa            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|     chinese (simplified)      | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|     chinese (traditional)     | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|           corsican            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|           croatian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|             czech             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|            danish             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|            divehi             |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |
|             dutch             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|            english            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|           esperanto           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|           estonian            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|            fijian             |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |
|           filipino            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            finnish            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|            french             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|            frisian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|           galician            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|           georgian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            german             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|             greek             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|           gujarati            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|        haitian creole         | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|             hausa             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|           hawaiian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|            hebrew             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|             hindi             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
|             hmong             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|           hungarian           | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|           icelandic           | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|             igbo              | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|          indonesian           | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
|           inuktitut           |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |
|             irish             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
|            italian            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|           japanese            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|           javanese            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|            kannada            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            kazakh             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|             khmer             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|          kinyarwanda          | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|            korean             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
|            kurdish            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            kyrgyz             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|              lao              | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|             latin             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|            latvian            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|          lithuanian           | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|         luxembourgish         | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|          macedonian           | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|           malagasy            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|             malay             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|           malayalam           | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            maltese            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|             maori             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            marathi            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|           mongolian           | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            myanmar            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|            nepali             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|           norwegian           | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|             odia              | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            pashto             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            persian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            polish             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|          portuguese           | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|            punjabi            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|           romanian            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|            russian            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|            samoan             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|         scots gaelic          | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|            serbian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            sesotho            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|             shona             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|            sindhi             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|            sinhala            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|            slovak             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|           slovenian           | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|            somali             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|            spanish            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|           sundanese           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|            swahili            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            swedish            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|           tahitian            |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |
|             tajik             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|             tamil             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|             tatar             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            telugu             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|             thai              | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            tibetan            |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |
|           tigrinya            |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |
|             tonga             |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |
|            turkish            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
|            turkmen            | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|           ukrainian           | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|             urdu              | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|            uyghur             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|             uzbek             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|          vietnamese           | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: | :heavy_check_mark: |
|             welsh             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |
|             xhosa             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|            yiddish            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|            yoruba             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
|             zulu              | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |
| **Total supported languages** |      **109**       |      **109**       |       **24**       |      **105**       |       **17**       |

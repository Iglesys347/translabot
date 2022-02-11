# Translabot

Discord bot for message translation in different languages.

![Bot image](ressources/translabot_white.png)

## Supported languages

The languages supported depend on the type of translator used. The available translators are the ones implemented in [deep-transaltor repo](https://github.com/nidhaloff/deep-translator):

- [Google Translate](https://translate.google.com)
- [Mymemory](https://mymemory.translated.net)
- [DeepL](https://www.deepl.com/translator) (API key needed)
- [QCRI](https://mt.qcri.org/api) (API key needed)
- [Microsoft Translator](https://www.microsoft.com/translator/) (API key needed)
- [Papago](https://papago.naver.com/) (client ID and client secret key needed)
- [Libre Translate](https://libretranslate.com/)

The basic configuration uses the Google Translate translator.

Here is a summary table of the languages supported by each translator:

|           Language            |       Google       |      Mymemory      |       Deepl        |        QCRI        |     Microsoft      |       Papago       |       Libre        |
| :---------------------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: |
|           afrikaans           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           albanian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            amharic            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            arabic             | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |
|           armenian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           assamese            |        :x:         |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|          azerbaijani          | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            bashkir            |        :x:         |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            basque             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|          belarusian           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|            bengali            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            bosnian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           bulgarian           | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            burmese            |        :x:         |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            catalan            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            cebuano            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|           chichewa            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|     chinese (simplified)      | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|     chinese (traditional)     | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|           corsican            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|           croatian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             czech             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            danish             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            divehi             |        :x:         |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             dutch             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            english            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|           esperanto           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|           estonian            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            fijian             |        :x:         |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           filipino            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            finnish            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            french             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|            frisian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|           galician            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|           georgian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            german             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         | :heavy_check_mark: |
|             greek             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           gujarati            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|        haitian creole         | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             hausa             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|           hawaiian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|            hebrew             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             hindi             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         | :heavy_check_mark: |
|             hmong             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|           hungarian           | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           icelandic           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             igbo              | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|          indonesian           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|           inuktitut           |        :x:         |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             irish             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         | :heavy_check_mark: |
|            italian            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         | :heavy_check_mark: |
|           japanese            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|           javanese            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|            kannada            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            kazakh             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             khmer             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|          kinyarwanda          | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|            korean             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|            kurdish            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            kyrgyz             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|              lao              | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             latin             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|            latvian            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|          lithuanian           | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|         luxembourgish         | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|          macedonian           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           malagasy            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             malay             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           malayalam           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            maltese            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             maori             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            marathi            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           mongolian           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            myanmar            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|            nepali             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           norwegian           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             odia              | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            pashto             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            persian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            polish             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         | :heavy_check_mark: |
|          portuguese           | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         | :heavy_check_mark: |
|            punjabi            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           romanian            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            russian            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         | :heavy_check_mark: |
|            samoan             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|         scots gaelic          | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|            serbian            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            sesotho            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|             shona             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|            sindhi             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|            sinhala            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|            slovak             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           slovenian           | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            somali             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|            spanish            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|           sundanese           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|            swahili            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            swedish            | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           tahitian            |        :x:         |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             tajik             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|             tamil             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             tatar             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            telugu             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             thai              | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
|            tibetan            |        :x:         |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           tigrinya            |        :x:         |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             tonga             |        :x:         |        :x:         |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            turkish            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         | :heavy_check_mark: |
|            turkmen            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|           ukrainian           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             urdu              | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|            uyghur             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             uzbek             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|          vietnamese           | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
|             welsh             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         | :heavy_check_mark: |        :x:         |        :x:         |
|             xhosa             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|            yiddish            | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|            yoruba             | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
|             zulu              | :heavy_check_mark: | :heavy_check_mark: |        :x:         |        :x:         |        :x:         |        :x:         |        :x:         |
| **Total supported languages** |      **109**       |      **109**       |       **24**       |       **3**        |      **105**       |       **10**       |       **17**       |

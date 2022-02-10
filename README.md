# Translabot

Discord bot for message translation in different languages.

![Bot image](ressources/translabot_white.png)

## Supported languages

The languages supported depend on the type of translator used. The available translators are the ones implemented in [deep-transaltor repo](https://github.com/nidhaloff/deep-translator):

- [Google Translate](https://translate.google.com)
- [Mymemory](https://mymemory.translated.net)
- [DeepL](https://www.deepl.com/translator) (API key needed)
- [QCRI](https://mt.qcri.org/api) (API key needed)
- [Yandex](https://translate.yandex.com/) (API key needed)
- [Microsoft Translator](https://www.microsoft.com/translator/) (API key needed)
- [Papago](https://papago.naver.com/) (client ID and client secret key needed)
- [Libre Translate](https://libretranslate.com/)

The basic configuration uses the Google Translate translator.

Here is a summary table of the languages supported by each translator:

| Language | Google | Mymemory | Deepl | QCRI | Yandex | Microsoft | Papago | Libre |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| afrikaans | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| albanian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| amharic | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| arabic | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| armenian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| azerbaijani | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| basque | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| belarusian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| bengali | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| bosnian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| bulgarian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| catalan | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| cebuano | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| chichewa | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| chinese (simplified) | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| chinese (traditional) | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| corsican | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| croatian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| czech | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| danish | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| dutch | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| english | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| esperanto | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| estonian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| filipino | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| finnish | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| french | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| frisian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| galician | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| georgian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| german | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| greek | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| gujarati | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| haitian creole | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| hausa | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| hawaiian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| hebrew | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| hindi | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| hmong | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| hungarian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| icelandic | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| igbo | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| indonesian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| irish | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| italian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| japanese | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| javanese | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| kannada | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| kazakh | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| khmer | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| kinyarwanda | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| korean | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| kurdish | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| kyrgyz | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| lao | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| latin | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| latvian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| lithuanian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| luxembourgish | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| macedonian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| malagasy | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| malay | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| malayalam | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| maltese | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| maori | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| marathi | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| mongolian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| myanmar | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| nepali | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| norwegian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| odia | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| pashto | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| persian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| polish | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| portuguese | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| punjabi | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| romanian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| russian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| samoan | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| scots gaelic | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| serbian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| sesotho | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| shona | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| sindhi | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| sinhala | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| slovak | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| slovenian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| somali | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| spanish | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| sundanese | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| swahili | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| swedish | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| tajik | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| tamil | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| tatar | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| telugu | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| thai | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| turkish | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| turkmen | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| ukrainian | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| urdu | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| uyghur | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| uzbek | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| vietnamese | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| welsh | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| xhosa | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| yiddish | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| yoruba | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
| zulu | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> | <ul><li>[x]</li> |
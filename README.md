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

|       Language        |       Google       |      Mymemory      |       Deepl        |        QCRI        |       Yandex       |     Microsoft      |       Papago       |       Libre        |
| :-------------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: |
|       afrikaans       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       albanian        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        amharic        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        arabic         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       armenian        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|      azerbaijani      | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        basque         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|      belarusian       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        bengali        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        bosnian        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       bulgarian       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        catalan        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        cebuano        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       chichewa        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
| chinese (simplified)  | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
| chinese (traditional) | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       corsican        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       croatian        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         czech         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        danish         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         dutch         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        english        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       esperanto       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       estonian        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       filipino        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        finnish        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        french         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        frisian        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       galician        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       georgian        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        german         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         greek         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       gujarati        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|    haitian creole     | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         hausa         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       hawaiian        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        hebrew         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         hindi         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         hmong         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       hungarian       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       icelandic       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         igbo          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|      indonesian       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         irish         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        italian        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       japanese        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       javanese        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        kannada        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        kazakh         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         khmer         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|      kinyarwanda      | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        korean         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        kurdish        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        kyrgyz         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|          lao          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         latin         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        latvian        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|      lithuanian       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|     luxembourgish     | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|      macedonian       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       malagasy        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         malay         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       malayalam       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        maltese        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         maori         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        marathi        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       mongolian       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        myanmar        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        nepali         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       norwegian       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         odia          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        pashto         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        persian        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        polish         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|      portuguese       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        punjabi        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       romanian        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        russian        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        samoan         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|     scots gaelic      | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        serbian        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        sesotho        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         shona         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        sindhi         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        sinhala        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        slovak         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       slovenian       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        somali         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        spanish        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       sundanese       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        swahili        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        swedish        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         tajik         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         tamil         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         tatar         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        telugu         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         thai          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        turkish        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        turkmen        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|       ukrainian       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         urdu          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        uyghur         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         uzbek         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|      vietnamese       | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         welsh         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         xhosa         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        yiddish        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|        yoruba         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
|         zulu          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |

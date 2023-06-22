from googletrans import Translator

def translateText(input, srcLang):
    translator = Translator()
    if srcLang == "ja":
        print("ja")
        return input
    translator = Translator()
    outcome = translator.translate(input, src = "english", dest = "japanese")
    translated = outcome.text
    return translated
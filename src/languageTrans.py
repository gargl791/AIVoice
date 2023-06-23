from googletrans import Translator
import whisper

#field variables
filename = "src/output.wav"
translator = Translator()
destLang = "japanese"
whisperModel = "tiny"

#Speech to text conversion of a sound file (.mp3, .wav etc)
model = whisper.load_model(whisperModel)


def transcribeFile(soundFile):
    global srcLang, outputText

    #Transcribes user voice input as text
    result = model.transcribe(soundFile, fp16 = False)

    #Speech to text output
    srcLang = result["language"]
    outputText = result["text"]
    return outputText


def translateText(input):
    if srcLang == "ja":
        print("ja")
        return input
    
    outcome = translator.translate(text = input, src = srcLang, dest = destLang)
    translated = outcome.text
    
    return translated

if __name__ == "__main__":
    text = transcribeFile("voice.wav")
    translateText(text)
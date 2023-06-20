from voicevox import Client
import googletrans
from googletrans import Translator
import asyncio

def translateText(input):
    translator = Translator()
    outcome = translator.translate(input, src = "english", dest = "japanese")
    translated = outcome.text
    return translated

resultSynth = translateText("Goofy ahh mf")

async def main():
    async with Client() as client:
        audio_query = await client.create_audio_query(
            resultSynth, speaker=54
        )
        with open("voice.wav", "wb") as f:
            f.write(await audio_query.synthesis(speaker=20))


if __name__ == "__main__":
    asyncio.run(main())




    
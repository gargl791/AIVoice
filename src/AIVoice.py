from voicevox import Client
import asyncio
import languageTrans
import whisper
from googletrans import Translator

#Speech to text conversion of a sound file (.mp3, .wav etc)
model = whisper.load_model("base")
result = model.transcribe("voice.wav", fp16 = False)

#Speech to text output
language = result["language"]
output = result["text"]


resultSynth = languageTrans.translateText(result["text"], language)

async def main():
    async with Client() as client:
        audio_query = await client.create_audio_query(
            resultSynth, speaker=54
        )
        with open("voice.mp3", "wb") as f:
            f.write(await audio_query.synthesis(speaker=20))


if __name__ == "__main__":
    asyncio.run(main())




    
from voicevox import Client
import asyncio

#field variables
speaker = 20; #check voicevox_speakers.json for speakers list


async def voiceConversion():
    async with Client() as client:
        audio_query = await client.create_audio_query(
            "バカ野郎、ぶっ飛ばしてやる", speaker = speaker
        )
        with open("voice.wav", "wb") as f:
            f.write(await audio_query.synthesis(speaker = speaker))


if __name__ == "__main__":
    asyncio.run(voiceConversion())


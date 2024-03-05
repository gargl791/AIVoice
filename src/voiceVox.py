from urllib.parse import urlencode
import requests

#Paste colab url here for voicevox
BASE_URL = "https://tangy-cars-film.loca.lt"

def speak_jp(sentence):
    # generate initial query
    params_encoded = urlencode({'text': sentence, 'speaker': 20})
    r = requests.post(BASE_URL)

    if r.status_code == 404:
        print('Unable to reach Voicevox, ensure that it is running, or the VOICEVOX_BASE_URL variable is set correctly')
        return

    voicevox_query = r.json()

    # synthesize voice as wav file
    params_encoded = urlencode({'speaker': 20})
    r = requests.post(BASE_URL)

    with open("tts.wav", 'wb') as outfile:
        outfile.write(r.content)

speak_jp("Hello")
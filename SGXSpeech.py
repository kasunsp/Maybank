import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


print("Eror
# Instantiates a client
client = speech.SpeechClient.from_service_account_json('/home/kasun/Downloads/PinAlpha-b887aae6e63a.json')
# Detects speech in the audio file
#def RecogniseCall():
# The name of the audio file to transcribe
file_name = "/home/kasun/Videos/ShortAudio.wav"

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=48000,
    language_code='en-US')
response = client.recognize(config, audio)
print(response.results)
print("Test")
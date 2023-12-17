from openai import OpenAI
from pathlib import Path
import os
from dotenv import load_dotenv
from audio import Recording

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
  api_key=api_key
)


audi_file = Recording()

audio_file = open(Path(__file__).parent / f"{audi_file}", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file,
  response_format="text"
)
print("Conversão para txt: ",transcript)
language = input("Digite para qual idioma quer traduzir: ")

text = transcript

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": f"Will you help me translate all the text after the special character '/' to the {language} language as an expert translator in it. Only return the translated text."},
    {"role": "user", "content": f"/ {text}"}
  ]
)

print(completion.choices[0].message.content)

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=f"{completion.choices[0].message.content}"
)

response.stream_to_file(speech_file_path)

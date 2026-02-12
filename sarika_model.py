import os
from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

response = client.speech_to_text.transcribe(
    file=open("output.wav", "rb"),
    model="saarika:v2.5",
    language_code="en-IN"
)

print(response)

import os
from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

response = client.text.translate(
    input="मैं ऑफिस जा रहा हूँ",
    source_language_code="hi-IN",
    target_language_code="mr-IN"
)

print(response)

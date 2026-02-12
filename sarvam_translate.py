import os
from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))

response = client.text.translate(
    input="भारत एक महान देश है। इसकी संस्कृति बहुत पुरानी और समृद्ध है।",
    source_language_code="hi-IN",
    target_language_code="en-IN",
    model="sarvam-translate:v1"
)

print(response)

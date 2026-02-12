import os
from dotenv import load_dotenv
from sarvamai import SarvamAI
from sarvamai.play import play, save

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

response = client.text_to_speech.convert(
    text="कृत्रिम बुद्धिमत्ता आधुनिक तकनीक का एक महत्वपूर्ण और तेज़ी से विकसित होने वाला क्षेत्र है।",
    target_language_code="hi-IN",
    model="bulbul:v3"
)

# Play the audio
play(response)

# Save the response to a file
save(response, "output1.wav")

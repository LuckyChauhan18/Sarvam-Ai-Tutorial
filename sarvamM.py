import os
from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY"),
)

response = client.chat.completions(
    messages=[
        {"role": "user", "content": "formula of quadratic equation"}
    ],
    temperature=0.2,
    top_p=1,
    max_tokens=1000,
)

print(response.choices[0].message.content)

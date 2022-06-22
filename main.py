from pathlib import Path
import json
import tweepy
import os
from auth import api
import ai

adviceAI = ai.AI(
    organization=os.environ["OPENAI_ORGANIZATION"],
    api_key=os.environ["OPENAI_API_KEY"],
    prompt=Path('prompt.txt').read_text(),
    temperature=0.9,
    max_tokens=128,
    presence_penalty=2,
    frequency_penalty=1.4,
    blacklisted_words=["nazi", "killing themselves", "kill yourself", "kill themselves", "retarded", "autistic", "suicide", "suicidal", "rape", "hitler"]
)

print("Starting...")
print("Generating advice...")
advice = adviceAI.generate_advice()
print(advice)
print("Tweeting...")
api.update_status(advice)
print("Successfully Tweeted")

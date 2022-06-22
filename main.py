from pathlib import Path

import json
import tweepy
from auth import api

import ai

settingsFile = open("settings.json")
settings = json.load(settingsFile)

adviceAI = ai.AI(
    organization=settings['openai_organization'],
    api_key=settings['openai_api_key'],
    prompt=Path('prompt.txt').read_text(),
    temperature=settings['ai_temperature'],
    max_tokens=settings['ai_max_tokens'],
    presence_penalty=settings['ai_presence_penalty'],
    frequency_penalty=settings['ai_frequency_penalty'],
    blacklisted_words=settings['blacklisted_words']
)

print("Starting...")

print("Generating advice...")
advice = adviceAI.generate_advice()
print(advice)
print("Tweeting...")
api.update_status(advice)
print("Successfully Tweeted")

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(f'{os.path.dirname(os.path.realpath(__file__))}/../.env')

client = OpenAI()

def get_prompt(input_lang, output_lang):
    return f'You are a translator. Translate user texts from {input_lang} to {output_lang}. Texts are in markdown format and your translation should also be in markdown. If you find any links or file paths do not alter them. Fix any grammatical error and any misinformation, but keep the style and vocabulary untouched. TEXT:'

def translate(text: str, input_lang, output_lang):
    if text.strip() == '':
        return text
    prompt = get_prompt(input_lang, output_lang)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ]
    )

    return '\n\n' + completion.choices[0].message.content

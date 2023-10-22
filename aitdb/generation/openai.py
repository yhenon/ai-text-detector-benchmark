import openai
from aitdb.generation import TextGenerator
import os


class OpenaiGenerator(TextGenerator):
    def __init__(self):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if openai_api_key is None:
            raise EnvironmentError("Openai API key not in environment, define OPENAI_API_KEY")
        openai.api_key = openai_api_key

        super().__init__()

    def generate(self, prompt: str):
        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "user", "content": prompt}
          ]
        )
        return completion.choices[0].message["content"]


from aitdb.generation.openai import OpenaiGenerator
from aitdb.classification.copyleaks import CopyleaksClassifier
from dotenv import load_dotenv

load_dotenv()

prompt = "explain molecular dynamics in 1-2 sentences"
print(f'The prompt is {prompt}')

gen = OpenaiGenerator()
out = gen.generate(prompt)
print(f'The generated text is: {out}')

cls = CopyleaksClassifier()
ai_prob = cls.classify(out)
print(f"AI probability: {ai_prob}")

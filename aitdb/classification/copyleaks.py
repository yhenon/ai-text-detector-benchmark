import requests
import json
from aitdb.classification import TextClassifier
import os


class CopyleaksClassifier(TextClassifier):
    def __init__(self):
        copyleaks_api_key = os.getenv("COPYLEAKS_API_KEY")
        if copyleaks_api_key is None:
            raise EnvironmentError("Copyleaks API key not in environment, define OPENAI_API_KEY")

        copyleaks_email = os.getenv("COPYLEAKS_EMAIL")
        if copyleaks_email is None:
            raise EnvironmentError("Copyleaks Email  not in environment, define COPYLEAKS_EMAIL")

        headers = {'Content-type': 'application/json'}
        myobj = json.dumps({'email': copyleaks_email, 'key': copyleaks_api_key})

        response = requests.post('https://id.copyleaks.com/v3/account/login/api', headers=headers, data=myobj)
        bearer_token = response.json()['access_token']

        self.headers = {'Content-type': 'application/json', 'Authorization': f'Bearer {bearer_token}'}
        super().__init__()

    def classify(self, prompt: str):
        myobj = json.dumps({'text': prompt, 'sandbox': 'true'})

        response = requests.post('https://api.copyleaks.com/v2/writer-detector/aitdb/check', headers=self.headers,
                                 data=myobj)
        ai_prob = response.json()['summary']['ai']
        return ai_prob

import requests
# pprint is used to format the JSON response
from pprint import pprint
import os

subscription_key = ""
endpoint = "https://qnamakerworkshopmai.azurewebsites.net/qnamaker"

# language detection
language_api_url = endpoint + "/knowledgebases/bbc18410-efc4-4756-b122-0bb87e2a08cb/generateAnswer"

question = {"question": "привет"}

headers = {"Authorization": subscription_key}
response = requests.post(language_api_url, headers=headers, json=question)
languages = response.json()
pprint(languages)
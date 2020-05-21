# -*- coding: utf-8 -*-
import os, requests, uuid, json

subscription_key = ''
endpoint = 'https://api.cognitive.microsofttranslator.com'

# that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
path = '/translate?api-version=3.0'
params = '&to=ru&to=en'
constructed_url = endpoint + path + params

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': 'Привет потомки'
}]
request = requests.post(constructed_url, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))

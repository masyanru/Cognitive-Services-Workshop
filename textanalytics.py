import requests
# pprint is used to format the JSON response
from pprint import pprint
import os

subscription_key = "1242c3d427ae452382c699390769b569"
endpoint = "https://textanalyticsworkshop.cognitiveservices.azure.com"

# language detection
language_api_url = endpoint + "/text/analytics/v2.1/languages"

documents = {"documents": [
    {"id": "1", "text": "This is a document written in English."},
    {"id": "2", "text": "Este es un document escrito en Español."},
    {"id": "3", "text": "这是一个用中文写的文件"},
    {"id": "4", "text": "Этот текст написан на русском."}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)


# sentiment

sentiment_url = endpoint + "/text/analytics/v2.1/sentiment"

documents = {"documents": [
    {"id": "1", "language": "en",
        "text": "I had a wonderful experience! The rooms were wonderful and the staff was helpful."},
    {"id": "2", "language": "en",
        "text": "I had a terrible time at the hotel. The staff was rude and the food was awful."},
    {"id": "3", "language": "es",
        "text": "Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos."},
    {"id": "4", "language": "es",
     "text": "La carretera estaba atascada. Había mucho tráfico el día de ayer."},
    {"id": "5", "language": "ru",
     "text": "Я прекрасно провёл время в вашем отеля. Огромное спасибо."},
    {"id": "6", "language": "ru",
     "text": "Хуже просто некуда, полный отстой, сервис сутками лежит, хватит уже мучать пользователей."}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(sentiment_url, headers=headers, json=documents)
sentiments = response.json()
pprint(sentiments)


# Extract key phrases
keyphrase_url = endpoint + "/text/analytics/v2.1/keyphrases"

documents = {"documents": [
    {"id": "1", "language": "en",
        "text": "I had a wonderful experience! The rooms were wonderful and the staff was helpful."},
    {"id": "2", "language": "en",
        "text": "I had a terrible time at the hotel. The staff was rude and the food was awful."},
    {"id": "3", "language": "es",
        "text": "Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos."},
    {"id": "4", "language": "es",
     "text": "La carretera estaba atascada. Había mucho tráfico el día de ayer."},
    {"id": "5", "language": "ru",
     "text": "Я прекрасно провёл время в вашем отеля. Огромное спасибо."},
    {"id": "6", "language": "ru",
     "text": "Хуже просто некуда, полный отстой, сервис сутками лежит, хватит уже мучать пользователей."}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(keyphrase_url, headers=headers, json=documents)
key_phrases = response.json()
pprint(key_phrases)

# Identify Entities
entities_url = endpoint + "/text/analytics/v2.1/entities"
documents = {"documents": [
    {"id": "1", "text": "Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975, to develop and sell BASIC interpreters for the Altair 8800."},
    {"id": "2", "language": "ru", "text": "Компания начинает свою историю с 1975 года, когда друзья-студенты Гарварда Билл Гейтс и Пол Аллен, прочитав опубликованную 1 января 1975 года в журнале «Popular Electronics (англ.)» статью о новом персональном компьютере Altair 8800, разработали для него интерпретатор языка Basic."}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(entities_url, headers=headers, json=documents)
entities = response.json()
pprint(entities)




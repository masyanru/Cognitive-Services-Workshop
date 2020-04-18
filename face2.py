import requests
import json

# set to your own subscription key value
subscription_key = '9bb017d33b6d426ea26400eadffeeafa'
assert subscription_key

# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = 'https://cognitivefaceworkshop.cognitiveservices.azure.com/face/v1.0/detect'

image_url = 'https://pbs.twimg.com/profile_images/1221837516816306177/_Ld4un5A_400x400.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
print(json.dumps(response.json()))

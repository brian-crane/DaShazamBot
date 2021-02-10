
import praw
import requests
import Private

print("I'm back baby.")




data = {
    'api_token': Private.get_api_key(),
    'return': 'apple_music,spotify',
}
files = {
    'file': open('hello.mp3', 'rb'),
}
result = requests.post('https://api.audd.io/', data=data, files=files)
print(result.text)
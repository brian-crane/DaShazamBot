
import praw

print("I'm back baby.")




import requests
data = {
    'api_token': '4d8b1af478dfc4bbbeedec82e9878560',
    'return': 'apple_music,spotify',
}
files = {
    'file': open('hello.mp3', 'rb'),
}
result = requests.post('https://api.audd.io/', data=data, files=files)
print(result.text)
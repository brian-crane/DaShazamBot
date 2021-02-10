import requests
from private import Private


# Accepts the fileName of an mp3 and sends it to AUD
# Will return a <Success(bool), Details(String)> Response
def post_song(mp3):
    data = {
        'api_token': Private.get_api_key(),
        'return': 'apple_music,spotify',
    }
    files = {
        'file': open(mp3, 'rb'),
    }
    return requests.post('https://api.audd.io/', data=data, files=files).text

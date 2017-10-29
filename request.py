import random
import json
import requests


def pick_clip_random():
    """
    pick a random clip from <url>
    """
    url = 'https://api.twitch.tv/kraken/clips/top'
    parms = {
        'channel': 'kamet0',
        'period': 'all'
    }
    headers = {
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Client-ID': '6agi3wajd7fjqixf5wp9mzof4q8d0b'
    }

    res = requests.get(url, params=parms, headers=headers)

    json_res = res.json()

    return random.choice(json_res['clips'])['url']

import asyncio
import aiohttp
import random

async def request_to_future(future, session, *session_args, **session_kwargs):
    async with session.request(*session_args, **session_kwargs) as resp:
        future.set_result(await resp.json())

http = aiohttp.ClientSession()
clips = asyncio.Future()
asyncio.ensure_future(request_to_future(clips, http, 'get', 'https://api.twitch.tv/kraken/clips/top', 
            params = {'channel': 'kamet0', 'period': 'all'},
            headers = {'Accept': 'application/vnd.twitchtv.v5+json', 'Client-ID': '6agi3wajd7fjqixf5wp9mzof4q8d0b'}))

async def use_clips():
    result =  clips.result()
    return random.choice(result['clips'])['url']
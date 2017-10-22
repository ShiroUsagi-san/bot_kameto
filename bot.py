from contextlib import suppress
import asyncio
import config
import discord


class Bot:
    _callbacks = {}
    

    def __init__(self, prefix):
        self.client = discord.Client()
        self.server = config.Config(1, "config.json")
        self.token = self.server.get_token()
        self.version = self.server.get_version()
        self.prefix = prefix

    def get_lib_version(self):
        return discord.__version__

    def run(self):
        self.client.run(self.server.get_token())

    async def react(self, message):
        msg = message.content
        """ if the message isn't prefixed, we dont go further"""
        if not msg.startswith(self.prefix):
            return

        cmd, *args = msg.split()
        cmd = cmd.lstrip(self.prefix)
        with suppress(KeyError):
            await self._callbacks[cmd](self, self.client, message, *args)

    @classmethod
    def register_cmd(cls, callback):
        cls._callbacks[callback.__name__] = callback
        return callback
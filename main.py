import logging
import config
import discord
import asyncio
import commands
import bot
logger = logging.getLogger(__name__)


def main():
    bot_test = bot.Bot('?')
    
    @bot_test.client.event
    async def on_ready():
        print("THE BOT IS UP")
        logger.info("THE BOT WAKES UP")
        logger.info("----------------")
    @bot_test.client.event
    async def on_message(message):
        await  bot_test.react(message)
        
    bot_test.run()





if __name__ == "__main__":
    main()
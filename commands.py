from bot import Bot
import asyncio
import discord
import random


"""
messages colors level
"""
info    = 0x0004ff
warning = 0xb71717
confirm = 0x17b737

@Bot.register_cmd
async def ping(bot, client, message):
    """
    Usage: ?ping
    repond pong!
    """
    await client.send_message(message.channel, '{0.mention} pong!'.format(message.author)) 


@Bot.register_cmd
async def liste(bot, client, message):
    """
    Usage: ?ls
    Liste toutes les commandes
    """
    await client.send_message(message.channel, '{0.mention}'.format(message.author))
    res = discord.Embed(title='Liste des commandes\n', description= '\n'.join(sorted(bot._callbacks.keys())), colour=info)
    await client.send_message(message.channel,embed=res)

@Bot.register_cmd
async def kameto(bot, client, message, *args):
    """
    Usage: ?kameto [type]
    permet de generer [type] au hasard
    """

    if args[0] == "phrase":
        f = open('random_phrases.txt', 'rt')
        data = f.read().split('\n')
        choice = random.choice(data)
        f.close()
        await client.send_message(message.channel, '{0.mention} {1}'.format(message.author, choice))
    elif args[0] == "image":
        pass
        #todo
    elif args[0] == "clip":
        pass
         #todo
    else:
        await client.send_message(message.channel, '{0.mention} cette option n\'existe pas'.format(message.author))
        
@Bot.register_cmd
async def aide(bot, client, message, cmd=None, *args):
    """
    Usage: ?aide [commande]
    obtenir de l'aide sur une commande
    """
    if not cmd:
        res = discord.Embed(description="\nEntrez '?aide <commande>' pour obtenir des informations sur <commande>\nEntrez ?liste pour avoir la liste des commandes.", colour=warning)
        await client.send_message(message.channel, embed=res)
        return
    cmd = bot._callbacks.get(cmd, None)
    if cmd is None:
        await liste(bot, client, message)
        return
    doc = cmd.__doc__
    if not doc:
        return

    help_format = '{0}'.format('\n'.join(line.strip() for line in doc.strip().split('\n')))
    help_embed = discord.Embed(title='{0}\n'.format(cmd.__name__), description=help_format, colour=info)
    await client.send_message(message.channel, embed=help_embed)

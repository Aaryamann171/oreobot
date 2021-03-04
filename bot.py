import os
import random
from twitchio.ext import commands

bot = commands.Bot(
        # initial setup
        irc_token=os.environ['TMI_TOKEN'],
        client_id=os.environ['CLIENT_ID'],
        nick=os.environ['BOT_NICK'],
        prefix=os.environ['BOT_PREFIX'],
        initial_channels=[os.environ['CHANNEL']]
)

@bot.event
async def event_ready():
    'Called once when the bot goes online'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    # if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
    #     return
    # await ctx.channel.send(ctx.content)

    # handle commands
    await bot.handle_commands(ctx)

    if 'hello' in ctx.content.lower():
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")

@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')

@bot.command(name='dice')
async def dice(ctx):
    dice_val = random.randint(1,6)
    await ctx.send(f'Dice says: {dice_val}')

@bot.command(name='coinflip')
async def coinflip(ctx):
    r = random.randint(0,1)
    toss_val = "Tails" if r else "Heads"
    await ctx.send(f'Coin says: {toss_val}')

if __name__ == "__main__":
    bot.run()

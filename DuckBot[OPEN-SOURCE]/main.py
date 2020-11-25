# Imports
import discord
from discord.ext import commands
import asyncio
import random
from pexels_api import API

# API Keys & Tokens
PEXELS_API_KEY = ' [ Insert API Key (Available @ https://www.pexels.com/api/) ] '
api = API(PEXELS_API_KEY)
TOKEN = " [ Insert Discord Bot Token (Available from the Discord Developer Portal) ] "

# Sets the prefix command, (can be changed)
client = commands.Bot(command_prefix = ':')

# Bot Status
async def status_task():
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="YOU! || :h for help"))
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the ducklings! || :h for help"))
        await asyncio.sleep(5)

# System Log Status Info
@client.event
async def on_ready():
    client.loop.create_task(status_task())
    print('------')
    print('DuckBot: Ready')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Created by torrylol')
    print('------')
    print('live update test')
    print('Created by torrylol')

# Bot Join Message (Server)
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            joined = await channel.send('Duck Bot has joined the server! || :h for help || 🦆 || Created by torrylol on https://github.com')
            await joined.add_reaction('🇭')
            await joined.add_reaction('🇮')
            await joined.add_reaction('🦆')

        break

# Duck key word reply
@client.event
async def on_message(message):

    duck_word = "duck"

    for duck_word in duck_word:
        if duck_word in message.content.lower():
            if message.author == client.user:
                return
            if ":" in message.content:
                await client.process_commands(message)
                break
            await message.channel.send(f'{message.author.mention} 🦆')
            break
        else:
            await client.process_commands(message)
            break

# help Command
@client.command()
async def h(ctx):
    help_message = await ctx.send('```fix\nDuck Help! *quack*\n\n A duck a day keeps the Lars away! \n   Created by torrylol on GIT lol \n\nCommands List: \n :duckpic || Sends a duck from the DUCK DATABASE \n :duckgif || Sends discord duck gif \n :pin || Kian Duck Pin \n :quack + message || Quack echo \n :gang + number || Summons the duck gang \n :tame + number || Tame a duck! \n :pdf [NEW] || Ducks1.pdf \n :fact [NEW] || Random Duck fact \n :alert + message || Alert! \n\nOther Features: \n - @Mention for "duck" keyword \n - Watches YOU (and the ducklings) \n - More features coming soon! \n\nCurrent Version; v.1.0.3```')
    await help_message.add_reaction('🇩')
    await help_message.add_reaction('🇺')
    await help_message.add_reaction('🇨')
    await help_message.add_reaction('🇰')
    await help_message.add_reaction('🦆')
    await help_message.add_reaction('🇧')
    await help_message.add_reaction('🇴')
    await help_message.add_reaction('🇹')
    await help_message.add_reaction('🤖')
    await help_message.add_reaction('🇭')
    await help_message.add_reaction('🇪')
    await help_message.add_reaction('🇱')
    await help_message.add_reaction('🇵')
    await help_message.add_reaction('✅')

@client.command()
async def duckpic(ctx):
    api.search('duck', page=1, results_per_page=500)
    photos = api.get_entries()
    chosen_duck = random.choice(photos)
    await ctx.send('Here! Take a duck pic')
    await ctx.send(chosen_duck.url)

@client.command()
async def duckgif(ctx):
    gif_choice = random.choice(['https://tenor.com/view/shake-wiggle-baby-animal-easter-gif-13928289', 'https://tenor.com/view/duck-ducky-lolol-pet-silly-gif-17203091', 'https://tenor.com/view/cute-duck-cuddle-its-ok-adorable-duck-gif-12985802', 'https://tenor.com/view/duck-run-panic-gif-5295491', 'https://tenor.com/view/duck-ducks-swing-cute-animals-gif-15449339', 'https://tenor.com/view/drumming-duck-drum-step-rhythm-gif-16192791', 'https://tenor.com/view/duck-fall-back-cute-falling-jump-gif-15884158'])
    await ctx.send('Here! Take a duck gif')
    await ctx.send(gif_choice)

@client.command()
async def pin(ctx):
    await ctx.send('! ! !      ↓ ↓ ↓ KIAN DUCK PIN ↓ ↓ ↓      ! ! !')
    pin_image = await ctx.send('https://cdn.discordapp.com/attachments/745072609019822131/745077083042218014/pin.jpg')
    await ctx.send('! ! !      ↑ ↑ ↑ KIAN DUCK PIN ↑ ↑ ↑      ! ! !')
    await pin_image.add_reaction('😍')
    await pin_image.add_reaction('🦆')
    await pin_image.add_reaction('🍉')
    await pin_image.add_reaction('📌')
    await pin_image.add_reaction('😻')
    await pin_image.add_reaction('🔪')

@client.command(pass_context=True)
async def quack(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('``*quack*`   ' + (message) + '   `*quack*`')

@client.command()
async def gang(ctx, arg):
    gang_amount = int(arg)
    gang_amount = "🦆"*gang_amount
    await ctx.send("😎 Duck Gang 😎")
    await ctx.send(gang_amount)
    await ctx.send("😎 Duck Gang 😎")

@client.command()
async def tame(ctx, arg):
    tame_amount = int(arg)
    tame_amount = "🍉" * tame_amount
    await ctx.send(tame_amount)
    await ctx.send('Watermelon released! Ducks can appear anywhere between 5-15 seconds, please be patient!')
    delay = random.randint(5,15)
    await asyncio.sleep(delay)
    delay = random.randint(5, 10)
    duck_found = random.randint(1, 15)
    await ctx.send(f'{ctx.author.mention} Thanks to your watermelon, ducks have been found! Duck Count: ' + str(duck_found))

@client.command()
async def pdf(ctx):
    await ctx.send('Ducks1.pdf, courtesy of Duck Bot')
    await ctx.send('https://cdn.discordapp.com/attachments/745072609019822131/745077077707063326/Ducks1.pdf')

@client.command()
async def fact(ctx):
    await ctx.send('Random Duck Fact:')
    fact = random.choice(['When a duckling hatches it has a downy plumage.', 'A duckling grows outer feathers by 5–8 weeks of age.', 'In late summer ducks lose all their feathers (called moulting) and grow new feathers.', 'When new feathers grow many ducks fly (migrate) to warmer lands for the winter.', 'Ducks have an oil gland at the base of their tail, which they use to water-proof their outer', 'feathers to protect them against the cold water.', 'Under the outer layer of feathers is a soft layer of small curly feathers called down.', 'Down feathers trap air under the outside feathers keeping the duck warm.', 'Ducks are generally monogamous although this bond may only last one year.', 'Only the female of “dabbling ducks” quack. The males never “quack”.', 'Most ducks breed once a year and tend to make a nest before breeding.', 'Not all ducks have the same incubation period – mallard varieties are generally 26-29 days and Muscovy ducks are 33-35 days.', 'Ducks feed on a variety of food – grasses, aquatic plants, fish, insects, small amphibians, worms and small molluscs.', 'Ducks live from 2 – 20 years.', 'Ducks are related to geese and swans.', 'Ducks, geese and swans have webbed feet and spread their toes and webbing which makes a paddle to swim with.', 'Contrary to popular belief, ducks do not require a pond or other open water in which to swim.', 'Ducks are not subject to parasites, fleas or ticks.', 'Because an idle floating duck or a duck squatting on land cannot react or move quickly, “a sitting duck” has come to mean “an easy target”.'])
    fact_sent = await ctx.send(fact)
    await fact_sent.add_reaction('🦆')
    await fact_sent.add_reaction('🇫')
    await fact_sent.add_reaction('🇦')
    await fact_sent.add_reaction('🇨')
    await fact_sent.add_reaction('🇹')

@client.command(pass_context=True)
async def alert(ctx, *, message):
    await ctx.message.delete()
    alerted = await ctx.send('🚨📣 ' + (message) + ' Alert!  📣🚨')
    await alerted.add_reaction('🇼')
    await alerted.add_reaction('🇴')
    await alerted.add_reaction('🇦')
    await alerted.add_reaction('🇭')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Duck Error: Please enter missing values!')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Insufficient Permissions")

client.run(TOKEN)


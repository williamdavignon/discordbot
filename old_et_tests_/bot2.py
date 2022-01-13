import discord, os, json

with open("token.txt", "r") as tokenfile:
    for line in tokenfile:
        token = line
client = discord.Client()
server = "745059328674758688"
bot = client
# bot = 751437378895347763

# score: {
#     "nom": "",
#     "pJ": "",
#     "v": "",
#     "pourc": "",
# }
ls = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
#     ls = 0
#     for m in server:
#         ls += m.members
#     print(ls)               

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!catan'):
        await message.channel.send('En construction!')

# @bot.command(pass_context=True) 
@client.event 
async def on_ready():
    for member in discord.utils.get(client.servers, id=server):
        print(member)
        for role in member.roles: 
            if role.name == "joueur":
                print("good")
            else:
                print("bad")
                




client.run(token)
import discord, os, json, requests
from discord.ext import commands
from bs4 import BeautifulSoup

with open("token.txt", "r") as tokenfile:
    for line in tokenfile:
        token = line
    
client = discord.Client()
server = "745059328674758688"
bot = commands.Bot(command_prefix="!")
url = "https://colonist.io/api/profile/"
formatage = ["GrandDude      ", "Ed14                  ", "MathCaramba  ", "manuuu              ", "Tinoz               "]
cookie = {"cookie": """Indicative_a38719f2-d919-446b-b2e3-0da55a22a29a="%7B%22defaultUniqueID%22%3A%223cb1d7f9-d96a-45b0-95b3-d1eaeecd6690%22%7D"; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIzODg5NzUyIiwiaWF0IjoxNTk5MzM2Mjc2LCJleHAiOjE2MDE5MjgyNzYsImF1ZCI6Imh0dHBzOi8vY29sb25pc3QuaW8vIiwiaXNzIjoiaHR0cHM6Ly9jb2xvbmlzdC5pby8ifQ.6Ovd1jP19LEhnMLjmxeDIsNvRPtL2Gta6WH_f8DkhZ8; userFromEEA=false; __qca=P0-347186434-1598322716806; __gads=ID=47c26a46075b17df:T=1598322717:S=ALNI_MZyQOzMMmkRuHDDjqLOd6_TN_SuAQ; cto_bundle=u3QW1l9xMURZazFEZTRoakNIZFFzdlZkRjdlS0d0UTRwcUZqdWtRUiUyQmh0Mk5MUm9zeVBkVVU0SVVjWWozdkRSaXBUMmNWZ1NTSFJxWkxaTDI0eTFIa282QXBQRm5LcmZEZDlvZHdEeEo3ZGZjOW1ianQ2NHA1QSUyQlluV1VsajlXT2lvWWtUczRGVERyOTNzVW9Wd25HTTdRQjZRJTNEJTNE; _ga=GA1.2.1923694805.1598324618; __cfduid=d131ebceea9ff7a81fb27457f95fc6ac11599175110"""}

#update de la user list
users = []
with open('users.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentUser = line[:-1]

        # add item to the list
        users.append(currentUser)

#var stats overall
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

        #update liste d'utilisateurs (define users)

        users = []
        with open('users.txt', 'r') as filehandle:
            for line in filehandle:
                # remove linebreak which is the last character of the string
                currentUser = line[:-1]

                # add item to the list
                users.append(currentUser)

        #AIDE

        if message.content == ("!catan"):
            f = open('help.text', "r")
            for line in f:
                print(line)
                await message.channel.send(line)
            f.close()

        #LISTE D'UTILISATEURS
        if message.content.startswith("!catan users"):
            #update la liste
            print(users)
            await message.channel.send(users)

        #ajout d'utilisateurs
        if message.content.startswith("!catan user add"):
            newuser = message.content
            newuser = newuser.split()
            newuser = newuser[3]
            # print(newuser)
            with open("users.txt", 'a') as filehandle:
                filehandle.write('%s\n' % newuser)
                await message.channel.send(newuser + " est ajouté à la liste!")
        
        #delete users
        if message.content.startswith("!catan user remove"):
            olduser = message.content
            olduser = olduser.split()
            olduser = olduser[3]
            with open("users.txt", "r") as f:
                lines = f.readlines()
            with open("users.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != olduser:
                        f.write(line)
            await message.channel.send(olduser + " est retiré de la liste.")



        #STATS OVERALL

        if message.content.startswith("!catan overall"):
            x = 0
            await message.channel.send("Statisque de la ligue Catanesque Grand Dude Extravaganza")
            await message.channel.send(" Utilisateur         V     PJ     PTS     %")
            for user in users:
                url2 = url + user
                # print(url2)
                site = requests.get(url2, cookies = cookie)
                if site.status_code == 200:
                    # print(site.text)
                    data = site.json()
                    v = data["totalWins"]
                    pj = data["totalGames"]
                    pts = data["totalPoints"]
                    pourc = v/pj*100
                    pourc = str(pourc)
                    pourc = pourc[0:4]
                    # espace = "-" * (18 - len(user))
                    # print(data)
                    # print(type(data)) 
                    # print("Statisques de " + user)
                    # print("Victoire:" + str(v))
                    # print("Parties jouées:"+ str(pj))
                    # print("Points totals:"+str(pts))
                    # print("Ratio de victoire " + str(pourc))
                    await message.channel.send( formatage[x] + str(v) + "    " + str(pj) +"    " +str(pts) + "    " +str(pourc)) 
                    x += 1  
                else: 
                    await message.channel.send(user + " n'est pas reconnu.")
                    print(user + " n'est pas reconnu.")
                    x += 1
                #fin overall stats



        #STATS COMPARATIVES
        if message.content.startswith("!catan comp"):
            print("catan comp")
            msg =str(message.content)
            msg = msg.split()
            joueur1 = msg[2]
            joueur2 = msg[3]
            url2 = url + joueur1
            site = requests.get(url2, cookies = cookie)
            data = site.json()
            histo = data["gameDatas"]
            total1 = 0
            total2 = 0
            totalpts1 = 0
            totalpts2 = 0
            for game in histo:
                ls = []
                playerrank = []
                bigrank = []
                players = game["players"]
                # print(players)
                # print(type(players))
                for player in players:
                    playerrank.append(player["username"])
                    playerrank.append(player["rank"])
                    bigrank.append(playerrank)
                    ls.append(player["username"])           #<-- liste des joueurs d'une partie
                # print(ls)
                # print(bigrank)
                if joueur2 in ls:
                    for player in players:
                        if joueur1 == player["username"]:
                            score1 = player["points"]
                            totalpts1 += score1
                            if player["rank"] == 1:
                                total1 += 1
                            # print(joueur1 + " : " + str(score1))
                        elif joueur2 == player["username"]:
                            score2 = player["points"]
                            totalpts2 += score2
                            # print(joueur2 + " : " + str(score2))
                            if player["rank"] == 1:
                                total2 += 1
            print(str(totalpts1) + "   " + str(totalpts2))
            # print(joueur1 + "wins" + str(total1) + "    " + joueur2 + "wins" + str(total2))
            if total1 == total2:
                print(joueur1 + " et " + joueur2 + "sont littéralement à égalité l'un contre l'autre, avec chacun "+ str(total1) + "victoires contre l'autre.")
                await message.channel.send(joueur1 + " et " + joueur2 + "sont littéralement à égalité l'un contre l'autre, avec chacun "+ str(total1) + "victoires contre l'autre.")
            if total1 > total2:
                print(joueur1 + " a scoré " + str(totalpts1) + " points contre " + joueur2 + ", qui en a scoré " + str(totalpts2)+".")
                print(joueur1 + " a gagné " + str(total1) + " fois contre " + joueur2 + ", alors que " + joueur2 + " a gagné seulement " + str(total2) + " fois contre " + joueur1 + ".")
                await message.channel.send(joueur1 + " a scoré " + str(totalpts1) + " points contre " + joueur2 + ", qui en a scoré " + str(totalpts2)+".")
                await message.channel.send(joueur1 + " a gagné " + str(total1) + " fois contre " + joueur2 + ", alors que " + joueur2 + " a gagné seulement " + str(total2) + " fois contre " + joueur1 + ".")
                if (total1 - total2) >= 2:
                    print(joueur1 + " pulvérise" + joueur2) 
                    await message.channel.send(joueur1 + " pulvérise" + joueur2) 
            if total2 > total1:
                print(joueur2 + " a scoré " + str(totalpts2) + " points contre " + joueur1 + ", qui en a scoré " + str(totalpts1)+".")
                print(joueur2 + " a gagné " + str(total2) + " fois contre " + joueur1 + ", alors que " + joueur1 + " a gagné seulement " + str(total1) + " fois contre " + joueur2 + ".")
                await message.channel.send(joueur2 + " a scoré " + str(totalpts2) + " points contre " + joueur1 + ", qui en a scoré " + str(totalpts1)+".")
                await message.channel.send(joueur2 + " a gagné " + str(total2) + " fois contre " + joueur1 + ", alors que " + joueur1 + " a gagné seulement " + str(total1) + " fois contre " + joueur2 + ".")
                if (total2 - total1) >= 2:
                    await message.channel.send(joueur2 + " pulvérise " + joueur1 + "!") 



client.run(token)
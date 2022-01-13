#coding: utf-8
import os, json, csv, requests, time, selenium
from bs4 import BeautifulSoup


fichier = "stats.csv"
url = "https://colonist.io/api/profile/"
# users = ["GrandDude"]
# users = ["GrandDude"]
users = ["GrandDude", "Ed14", "MathCaramba", "manuuu", "Tinoz"]
x = 0

cookie = {"cookie": """Indicative_a38719f2-d919-446b-b2e3-0da55a22a29a="%7B%22defaultUniqueID%22%3A%223cb1d7f9-d96a-45b0-95b3-d1eaeecd6690%22%7D"; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIzODg5NzUyIiwiaWF0IjoxNTk5MzM2Mjc2LCJleHAiOjE2MDE5MjgyNzYsImF1ZCI6Imh0dHBzOi8vY29sb25pc3QuaW8vIiwiaXNzIjoiaHR0cHM6Ly9jb2xvbmlzdC5pby8ifQ.6Ovd1jP19LEhnMLjmxeDIsNvRPtL2Gta6WH_f8DkhZ8; userFromEEA=false; __qca=P0-347186434-1598322716806; __gads=ID=47c26a46075b17df:T=1598322717:S=ALNI_MZyQOzMMmkRuHDDjqLOd6_TN_SuAQ; cto_bundle=u3QW1l9xMURZazFEZTRoakNIZFFzdlZkRjdlS0d0UTRwcUZqdWtRUiUyQmh0Mk5MUm9zeVBkVVU0SVVjWWozdkRSaXBUMmNWZ1NTSFJxWkxaTDI0eTFIa282QXBQRm5LcmZEZDlvZHdEeEo3ZGZjOW1ianQ2NHA1QSUyQlluV1VsajlXT2lvWWtUczRGVERyOTNzVW9Wd25HTTdRQjZRJTNEJTNE; _ga=GA1.2.1923694805.1598324618; __cfduid=d131ebceea9ff7a81fb27457f95fc6ac11599175110"""}
print("Outils de comparaison de deux joueurs")
joueur1 = input("Entrer le joueur 1:")
joueur2 = input("Enter le joueur 2:")
# print(joueur1 + joueur2)

url2 = url + joueur1
# print(url2)
site = requests.get(url2, cookies = cookie)
# print(site)
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
if total1 > total2:
    print(joueur1 + " a scoré " + str(totalpts1) + " points contre " + joueur2 + ", qui en a scoré " + str(totalpts2)+".")
    print(joueur1 + " a gagné " + str(total1) + " fois contre " + joueur2 + ", alors que " + joueur2 + " a gagné seulement " + str(total2) + " fois contre " + joueur1 + ".")
    if (total1 - total2) >= 2:
        print(joueur1 + " pulvérise" + joueur2) 
if total2 > total1:
    print(joueur2 + " a gagné " + str(total2) + " fois contre " + joueur1 + ", alors que " + joueur1 + " a gagné seulement " + str(total1) + " fois contre " + joueur2 + ".")
    if (total2 - total1) >= 2:
        print(joueur2 + " pulvérise " + joueur1 + "!") 
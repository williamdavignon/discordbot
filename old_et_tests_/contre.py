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
print("Historique des games contre")
# print(joueur1 + joueur2)
stats = []
players = []
# print(url2)
id_ = []
games = dict
fichier = "stats.csv"
dead = open(fichier, "w+")
# obies = csv.reader(dead)
# obies.truncate(0)
dead.close()

for user in users:
    dead = open(fichier, "a")
    obies = csv.writer(dead)
    obies.writerow([user])
    site = requests.get(url + user, cookies = cookie)
    data = site.json()
    histo = data["gameDatas"]
    for game in histo:
        if game["id"] in id_:
            print("no")
        else:
            id_.append(game["id"])
            players = []
            for player in game["players"]:
                players.append(player["username"])
            print(players)
            users_set = set(users)
            players_set = set(players)
            if len(users_set.intersection(players_set)) > 1:
                




print(id_)
print(len(id_))
print(len(games))

# a = [1, 2, 3, 4, 5, 6, 7] 
# b = [5, 6, 7, 8, 9] 
# a_set = set(a) 
# b_set = set(b) 
# x = a_set.intersection(b_set)
# print(x)
# print((len(x)))

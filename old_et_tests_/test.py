#coding: utf-8

import requests
cookie = {"cookie": """Indicative_a38719f2-d919-446b-b2e3-0da55a22a29a="%7B%22defaultUniqueID%22%3A%223cb1d7f9-d96a-45b0-95b3-d1eaeecd6690%22%7D"; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIzODg5NzUyIiwiaWF0IjoxNTk5MzM2Mjc2LCJleHAiOjE2MDE5MjgyNzYsImF1ZCI6Imh0dHBzOi8vY29sb25pc3QuaW8vIiwiaXNzIjoiaHR0cHM6Ly9jb2xvbmlzdC5pby8ifQ.6Ovd1jP19LEhnMLjmxeDIsNvRPtL2Gta6WH_f8DkhZ8; userFromEEA=false; __qca=P0-347186434-1598322716806; __gads=ID=47c26a46075b17df:T=1598322717:S=ALNI_MZyQOzMMmkRuHDDjqLOd6_TN_SuAQ; cto_bundle=u3QW1l9xMURZazFEZTRoakNIZFFzdlZkRjdlS0d0UTRwcUZqdWtRUiUyQmh0Mk5MUm9zeVBkVVU0SVVjWWozdkRSaXBUMmNWZ1NTSFJxWkxaTDI0eTFIa282QXBQRm5LcmZEZDlvZHdEeEo3ZGZjOW1ianQ2NHA1QSUyQlluV1VsajlXT2lvWWtUczRGVERyOTNzVW9Wd25HTTdRQjZRJTNEJTNE; _ga=GA1.2.1923694805.1598324618; __cfduid=d131ebceea9ff7a81fb27457f95fc6ac11599175110"""}

# x = "!catan user add Lukesh"
# print(type(x))
# x = x.split()
# print(type(x))
# print(x[3])
# x = x[3]

#any() test
# ls = [0,1,2,3,4]
# x = any(ls)
# print(x)

# #list 2 items checker

# a = [1, 2, 3, 4, 5, 6, 7] 
# b = [5, 6, 7, 8, 9] 
# a_set = set(a) 
# b_set = set(b) 
# x = a_set.intersection(b_set)
# print(x)
# print((len(x)))






# # token test
# with open("token.txt", "r") as tokenfile:
#     for line in tokenfile:
#         token = line

# print(token)


# status code test

# url1 = "https://colonist.io/api/profile/GrandDude"
# url2 = "https://colonist.io/api/profile/aodugnubqanifs"
# site = requests.get(url1, cookies = cookie)
# print(site.status_code)
# print(site)
# site = requests.get(url2, cookies = cookie)
# print(site.status_code)
# print(site)

#test avg rank
url1 = "https://colonist.io/api/profile/GrandDude"
url2 = "https://colonist.io/api/profile/aodugnubqanifs"
site = requests.get(url1, cookies = cookie)
# print(site.status_code)
# print(site)
# site = requests.get(url2, cookies = cookie)
# print(site.status_code)
# print(site)
user = "GrandDude"
data = site.json()
games = data["gameDatas"]
ttlrank= 0
ttlgames = 0
for game in games:
    ttlgames += 1
    for player in game["players"]:
        if player["username"] == user:
            ttlrank += int(player["rank"])
            avgrank = ttlrank/ttlgames
print(ttlrank)
print(avgrank)


# #print help
# f = open('help.text', "r")
# for line in f:
#     print(line)



# #delete
# with open("users.txt", "r") as f:
#     lines = f.readlines()
# with open("users.txt", "w") as f:
#     for line in lines:
#         if line.strip("\n") != "Lukesh":
#             f.write(line)





#add
# with open("users.txt", 'a') as filehandle:
#         filehandle.write('%s\n' % x)
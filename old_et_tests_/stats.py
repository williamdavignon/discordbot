#coding: utf-8
import os, json, csv, requests, time, selenium
from bs4 import BeautifulSoup
from selenium import webdriver


fichier = "stats.csv"
url = "http://colonist.io/profile/"
# users = ["GrandDude"]
users = ["Grandude", "Ed14", "MathCaramba", "manuuu", "Tinoz"]
x = 0

v = ""
pj = ""
pts = ""
pourc = ""

# from selenium import webdriver
# driver = webdriver.PhantomJS()
# # driver.get(my_url)
# p_element = driver.find_element_by_id(id_='intro-text')
# print(p_element.text)
# # # result:
# # 'Yay! Supports javascript'



# for user in users:
#     url2 = url + users[x]
#     x += 1
#     print(url2)
#     driver.get(url2)
#     # site = requests.get(url2, timeout = 5, headers = {"Connection":"keep-alive", "User-Agent":"Mozilla/5.0"})
#     # page = BeautifulSoup(site.text, "html.parser")
#     v = driver.find_element_by_id(id_="wins_stats")
#     print(v)
#     pj = driver.find_element_by_id(id_="games_stats")
#     print(pj)



for user in users:
    url2 = url + users[x]
    x += 1
    print(url2)
    site = requests.get(url2, timeout=(100, 1000), headers = {"Connection":"keep-alive", "User-Agent":"Mozilla/5.0"})
    time.sleep(1)
    page = BeautifulSoup(site.text, "html.parser")
    v = page.find("h5", id="wins_stats")
    print(v)
    pj = page.find("h5", id="games_stats")
    print(pj)

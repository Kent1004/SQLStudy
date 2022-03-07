import requests
import os
import time
#
# url = "https://api-football-v1.p.rapidapi.com/v3/leagues"
#
# querystring = {"id":"235","name":"Premier League","code":"RU"}
#
# headers = {
#     'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#     'x-rapidapi-key': "beed8a4c1bmsh05002244a643d21p1424dejsnb7058d2585ca"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)

# import requests
#
# url = "https://api-football-v1.p.rapidapi.com/v3/leagues"
#
# querystring = {"id":"235","name":"Premier League","season":"2021"}
#
# headers = {
#     'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#     'x-rapidapi-key': "beed8a4c1bmsh05002244a643d21p1424dejsnb7058d2585ca"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)

import http.client
#
# conn = http.client.HTTPSConnection("v3.football.api-sports.io")
#
# headers = {
#     'x-rapidapi-host': "v3.football.api-sports.io",
#     'x-rapidapi-key': "beed8a4c1bmsh05002244a643d21p1424dejsnb7058d2585ca"
#     }
#
# conn.request("GET", "/teams/statistics?season=2019&team=33&league=39", headers=headers)
#
# res = conn.getresponse()
# data = res.read()
#
# print(data.decode("utf-8"))
# '''Игры со счетом'''
# import requests
#
# url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
#
# querystring = {"league":"235","season":"2021"}
#
# headers = {
#     'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#     'x-rapidapi-key': "beed8a4c1bmsh05002244a643d21p1424dejsnb7058d2585ca"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)
# f = open('games.txt' , 'w+' )
# f.write(response.text)
# f.close()

# '''турнирная таблица'''
#
# import requests
#
# url = "https://api-football-v1.p.rapidapi.com/v3/standings"
#
# querystring = {"season":"2021","league":"235"}
#
# headers = {
#     'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#     'x-rapidapi-key': "beed8a4c1bmsh05002244a643d21p1424dejsnb7058d2585ca"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)
#
# f = open('standings.txt' , 'w+' )
# f.write(response.text)

# import requests
#
# url = "https://api-football-v1.p.rapidapi.com/v3/teams"
#
# querystring = {"season":"2021","league":"235"}
#
# headers = {
#     'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#     'x-rapidapi-key': "beed8a4c1bmsh05002244a643d21p1424dejsnb7058d2585ca"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)

#
# f = open('teams.txt' , 'w+' )
# f.write(response.text)
# f.close()


# import requests
# import time
#
url = "https://api-football-v1.p.rapidapi.com/v3/players"
f = open('players_2.txt' , 'w+' )
for i in range(1,31):
    time.sleep(4)
    print (i)
    querystring = {"league":"235","season":"2021","page":i}
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "beed8a4c1bmsh05002244a643d21p1424dejsnb7058d2585ca"
     }
    response = (requests.request("GET", url, headers=headers, params=querystring))
    # f.write(str(requests.request("GET", url, headers=headers, params=querystring)))
    f.write(response.text + '\n')

f.close()

'''Тренер по команде'''
import requests
# coaches = open('coaches1.txt' , 'w+' )
# l_team = ['555','558','596','597','621','779','1077','1078','1079','1083','1084','1085','1088','1994','2011','2012']
# url = "https://api-football-v1.p.rapidapi.com/v3/coachs"
# # print(l1)
# l=['555']
# querystring = {"team": l[0]}
# headers = {
#     'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#     'x-rapidapi-key': "beed8a4c1bmsh05002244a643d21p1424dejsnb7058d2585ca"
# }
# response = requests.request("GET", url, headers=headers, params=querystring)
# coaches.write(response.text + '\n')

# for i in range(0,len(l_team)):
#     print (i)
#     # time.sleep(7)
#     print(l_team[i])
#     querystring = {"team":l_team[i]}
#     headers = {
#         'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#         'x-rapidapi-key': "beed8a4c1bmsh05002244a643d21p1424dejsnb7058d2585ca"
#     }
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     print (response.text)
#     coaches.write(response.text + '\n')
#
#
# coaches.close()

# url = "https://api-football-v1.p.rapidapi.com/v3/players/topassists"
#
# querystring = {"league":"235","season":"2021"}
#
# headers = {
#        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
#         'x-rapidapi-key': "beed8a4c1bmsh05002244a643d21p1424dejsnb7058d2585ca"
#     }
#
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)
#
# f = open('topassists.txt' , 'w+' )
# f.write(response.text)
# f.close()


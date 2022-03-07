import json
from datetime import datetime

def dsum(*dicts):
    ret = {}
    ret  = dict(dicts[0])
    for k, v in dicts[1].items():
        if ret[k] == None: ret[k] = v
        elif v!= None and isinstance(v, int) :
            ret[k] += v
    return dict(ret)



str_stat = ''
str_stat1 = ''
str_stat2 = ''
stat_player = ''
player_list = []
statistics = open('9_statistics.sql', 'w+',encoding='utf-8')
with open('players_2.txt') as f:
    for obj in f:
        players_dict = json.loads(obj)
        player_list.append (players_dict)
# print
statistics.write (f'use soccer;' + '\n')
statistics.write (f'Drop table  if exists statistics;'+'\n')
statistics.write (f'Create table statistics ('+ '\n')
# str_stat+=
# print (player_list[0]["response"][0]['player']['id'])
str_stat1+='player_id, '
str_stat += 'player_id BIGINT PRIMARY KEY , '+'\n'

for k  in player_list[0]["response"][0]['statistics']:
    for k1,v1 in k.items():
        if isinstance(v1, dict) and (k1 == 'games' or k1 == 'goals' or k1 == 'penalty' or k1 == 'cards'):
            for k2, v2 in v1.items():
                str_stat1 += f'{k1}_{k2},'
                if k2 == 'captain':
                    str_stat+= f"{k1}_{k2} enum('true','false')," + '\n'
                elif isinstance(v2, int) or v2 == None:
                    str_stat += f"{k1}_{k2} INT," + '\n'
                elif isinstance(v2, str):
                    str_stat += f"{k1}_{k2} VARCHAR(255)," + '\n'

for l in player_list:
    for k,v in l.items():
        if k == 'response':
            for val in v:
                str_stat2 += '('
                str_stat2+= f"{val['player']['id']},"
                if len(val['statistics'])>1:
                    d_games = dsum  (val['statistics'][0]['games'], val['statistics'][1]['games'])
                    for k3,v3 in d_games.items():
                        if v3 == None :
                            str_stat2 += f'null,'
                        else: str_stat2 += f"'{v3}',"
                    d_goals = dsum(val['statistics'][0]['goals'], val['statistics'][1]['goals'])
                    for k3, v3 in d_goals.items():
                        if v3 == None:
                            str_stat2 += f'null,'
                        else:
                            str_stat2 += f"'{v3}',"
                    d_penalty = dsum(val['statistics'][0]['penalty'], val['statistics'][1]['penalty'])
                    for k3, v3 in d_penalty.items():
                        if v3 == None:
                            str_stat2 += f'null,'
                        else:
                            str_stat2 += f"'{v3}',"
                    d_cards = dsum(val['statistics'][0]['cards'], val['statistics'][1]['cards'])
                    for k3, v3 in d_cards.items():
                        if v3 == None:
                            str_stat2 += f'null,'
                        else:
                            str_stat2 += f"'{v3}',"

                else:
                    for l2 in val['statistics']:
                        # print (l2)
                        # print(f"{val['player']['id']}")
                        for k2,v2 in l2.items():
                            if k2 == 'games' or k2 == 'goals' or k2 == 'penalty' or k2 == 'cards':
                                for k3,v3 in v2.items():
                                    if v3 == None :
                                         str_stat2 += f'null,'
                                    else: str_stat2 += f"'{v3}',"
                str_stat2 = str_stat2 [:-1]
                str_stat2 += '),\n'

print (str_stat1)

statistics.write (str_stat[:-2]+');\n')

statistics.write ( f'Insert into statistics ({str_stat1[:-1]}) values' + '\n')
statistics.write (str_stat2[:-2]+';\n')
# print (unigue_player)
# a = str_stat2.splitlines()
# unique_rows = dict.fromkeys (a)
# unigue_player += "\n".join(unique_rows)
#
#
#
# player.write (str_stat[:-2] + ');\n')
# player.write(f'{unigue_player[:-2]}); ')
# player.write('\n')


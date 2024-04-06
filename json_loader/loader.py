import json
import os
import psycopg

seasons = ['2020/2021', '2019/2020', '2018/2019', '2003/2004']
conn = psycopg.connect(dbname='project_database', user='postgres', password=1234, host='localhost', port=5432)

#load data from competitions
competitions = json.load(open(os.getcwd() + '\json_loader\data\competitions.json', 'r'))

#filter competition data by season
competitionsList = []
competitionIds = []
seasonIds = []
for obj in competitions:
    if obj['season_name'] in seasons:
        competitionsList.append(obj)
        seasonIds.append(obj['season_id'])
        competitionIds.append(obj['competition_id'])

#load data into database
#for obj in competitionsList:
    #print(obj)


#load data from matches
matchesRoot = os.getcwd() + '\json_loader\data\matches'
matchObjects = []
matchIds = []
#filter competition folders in match folder
for file in os.listdir(matchesRoot):
    if int(file) not in competitionIds:
        continue
    
    #access contents (json files) of specific competition folder
    for match in os.listdir(os.path.join(matchesRoot, file)):
        if (int(match.split('.')[0]) not in seasonIds):
            continue
        matchData = json.load(open(os.path.join(matchesRoot, file, match), 'r', encoding='utf-8'))
        for obj in matchData:
            matchObjects.append(obj)
            matchIds.append(obj['match_id'])

#load match data into database
#for obj in matchObjects:
#    print(obj)
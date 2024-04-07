import json
import os
import psycopg

seasonsLaLiga = ['2020/2021', '2019/2020', '2018/2019']
seasonsPremierLeague = ['2003/2004']
competitionsTarget = ['Premier League', 'La Liga']
conn = psycopg.connect(dbname='project_database', user='postgres', password='1234', host='localhost', port='5432')
cur = conn.cursor()

#load data from competitions
competitions = json.load(open(os.getcwd() + '\json_loader\data\competitions.json', 'r'))

#filter competition data by season
competitionsList = []
competitionIds = []
seasonIds = []
for obj in competitions:
    if (obj['competition_name'] == 'Premier League') and (obj['season_name'] in seasonsPremierLeague):
        competitionsList.append(obj)
        seasonIds.append(obj['season_id'])
        competitionIds.append(obj['competition_id'])
    elif (obj['competition_name'] == 'La Liga') and (obj['season_name'] in seasonsLaLiga):
        competitionsList.append(obj)
        seasonIds.append(obj['season_id'])
        competitionIds.append(obj['competition_id'])

#load data into database
cur.execute('TRUNCATE TABLE Competitions CASCADE')
i = 0
for obj in competitionsList:
    cur.execute(
        "INSERT INTO Competitions (id, competition_id, competition_name, competition_gender, country_name, season_id, season_name) VALUES (%s,%s, %s, %s, %s, %s, %s)",
        (i, obj['competition_id'], obj['competition_name'], obj['competition_gender'], obj['country_name'], obj['season_id'], obj['season_name'])
    )
    i += 1
conn.commit()


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
            if obj['competition']['competition_id'] in competitionIds:
                matchObjects.append(obj)
                matchIds.append(obj['match_id'])

#load match data into database
#for obj in matchObjects:
#    print(obj)


#load data from events
eventsRoot = os.getcwd() + '\json_loader\data\events'
eventObjects = []
eventTypes = []

#filter events in events folder by match id                                               FORGET ABOUT THIS DO IT LATER
#for file in os.listdir(eventsRoot):
#    if int(file.split('.')[0]) not in matchIds:
#        continue
#
#    for event in json.load(open(os.path.join(eventsRoot, file), 'r', encoding='utf-8')):
#            eventObjects.append(event)
#            if (event['type']['name']) not in eventTypes:
#                eventTypes.append(event['type']['name'])


#load lineups data
lineupsRoot = os.getcwd() + '\json_loader\data\lineups'
lineupObjects = []

cur.close()
conn.close()
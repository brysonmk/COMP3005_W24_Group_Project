import json
import os
import psycopg

seasonsLaLiga = ['2020/2021', '2019/2020', '2018/2019']
seasonsPremierLeague = ['2003/2004']
competitionsTarget = ['Premier League', 'La Liga']
conn = psycopg.connect(dbname='project_database', user='postgres', password='1234', host='localhost', port='5432')
cur = conn.cursor()

#table creation
cur.execute(open(os.getcwd() + '\json_loader\loader.sql', 'r').read())
conn.commit()

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
seasonsList = ['2020/2021', '2019/2020', '2018/2019', '2003/2004']
for obj in matchObjects:
    i = seasonsList.index(obj['season']['season_name'])
    if 'referee' not in obj:
        obj['referee'] = {'id': None, 'name': None, 'country': {'id': None, 'name': None}}
    if 'managers' not in obj['home_team']:
        obj['home_team']['managers'] = [{'id': None, 'name': None, 'nickname': None, 'dob': None, 'country': {'id': None, 'name': None}}]
    if 'manager' not in obj['away_team']:
        obj['away_team']['managers'] = [{'id': None, 'name': None, 'nickname': None, 'dob': None, 'country': {'id': None, 'name': None}}]
    if 'stadium' not in obj:
        obj['stadium'] = {'id': None, 'name': None, 'country': {'id': None, 'name': None}}
    cur.execute(
        "INSERT INTO Matches (match_id, id, competition_id, competition_name, country_name, season_id, season_name, match_date, kick_off, stadium_id, stadium_name, stadium_country, referee_id, referee_name, referee_country_id, referee_country_name, home_team_id, home_team_name, home_team_gender, home_team_manager_id, home_team_manager_name, home_team_manager_nickname, home_team_manager_dob, home_team_manager_country_id, home_team_manager_country_name, home_team_group, home_team_country_id, home_team_country_name, away_team_id, away_team_name, away_team_gender, away_team_manager_id, away_team_manager_name, away_team_manager_nickname, away_team_manager_dob, away_team_manager_country_id, away_team_manager_country_name, away_team_group, away_team_country_id, away_team_country_name, home_score, away_score, match_status, match_week, competition_stage_id, competition_stage_name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (obj['match_id'], i, obj['competition']['competition_id'], obj['competition']['competition_name'], obj['competition']['country_name'], obj['season']['season_id'], obj['season']['season_name'], obj['match_date'], obj['kick_off'], obj['stadium']['id'], obj['stadium']['name'], obj['stadium']['country']['name'], obj['referee']['id'], obj['referee']['name'], obj['referee']['country']['id'], obj['referee']['country']['name'], obj['home_team']['home_team_id'], obj['home_team']['home_team_name'], obj['home_team']['home_team_gender'], obj['home_team']['managers'][0]['id'], obj['home_team']['managers'][0]['name'], obj['home_team']['managers'][0]['nickname'], obj['home_team']['managers'][0]['dob'], obj['home_team']['managers'][0]['country']['id'], obj['home_team']['managers'][0]['country']['name'], obj['home_team']['home_team_group'], obj['home_team']['country']['id'], obj['home_team']['country']['name'], obj['away_team']['away_team_id'], obj['away_team']['away_team_name'], obj['away_team']['away_team_gender'], obj['away_team']['managers'][0]['id'], obj['away_team']['managers'][0]['name'], obj['away_team']['managers'][0]['nickname'], obj['away_team']['managers'][0]['dob'], obj['away_team']['managers'][0]['country']['id'], obj['away_team']['managers'][0]['country']['name'], obj['away_team']['away_team_group'], obj['away_team']['country']['id'], obj['away_team']['country']['name'], obj['home_score'], obj['away_score'], obj['match_status'], obj['match_week'], obj['competition_stage']['id'], obj['competition_stage']['name'])
    )
conn.commit()


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
teamIds = []
playerIds = []
for lineup in os.listdir(lineupsRoot):
    if int(lineup.split('.')[0]) not in matchIds:
        continue
    for obj in json.load(open(os.path.join(lineupsRoot, lineup), 'r', encoding='utf-8')):
        lineupObjects.append(obj)


#load lineups data into database
for obj in lineupObjects:
    if obj['team_id'] not in teamIds:
        teamIds.append(obj['team_id'])
        #cur.execute() #insert team data into teams table
    for player in obj['lineup']:
        if player['player_id'] not in playerIds:
            playerIds.append(player['player_id'])
            #cur.execute() #insert player data into players table (along with team id they are apart of)

cur.close()
conn.close()
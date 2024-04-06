import json
import os
import psycopg

seasons = ['2020/2021', '2019/2020', '2018/2019', '2003/2004']
conn = psycopg.connect(dbname='project_database', user='postgres', password=1234, host='localhost', port=5432)

#load data from competitions
competitions = json.load(open(os.getcwd() + '\json_loader\data\competitions.json', 'r'))

#filter competition data by season
competitionsList = []
for obj in competitions:
    if obj['season_name'] in seasons:
        competitionsList.append(obj)

#load data into database
for obj in competitionsList:
    print(obj)

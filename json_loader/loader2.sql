DROP TABLE IF EXISTS Shots;
DROP TABLE IF EXISTS Passes;
DROP TABLE IF EXISTS Teams;
DROP TABLE IF EXISTS Players;

CREATE TABLE Shots (
    statsbomb_xg FLOAT PRIMARY KEY,
    player_id INTEGER UNIQUE,
    player_name INTEGER,
    team_id INTEGER UNIQUE,
    team_name INTEGER,
    first_time BOOLEAN
);

CREATE TABLE Passes (
    player_id INTEGER UNIQUE,
    player_name INTEGER,
    team_id INTEGER UNIQUE,
    team_name INTEGER,
    through_ball BOOLEAN,
    recipient VARCHAR(255)
);

CREATE TABLE Teams (
    team_id INTEGER UNIQUE,
    team_name INTEGER
);

CREATE TABLE Players (
    team_id INTEGER UNIQUE,
    player_id INTEGER UNIQUE,
    player_name INTEGER
);


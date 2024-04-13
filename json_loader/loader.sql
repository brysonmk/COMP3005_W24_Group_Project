DROP TABLE IF EXISTS Matches CASCADE;
DROP TABLE IF EXISTS Competitions CASCADE;
DROP TABLE IF EXISTS Shots CASCADE;
DROP TABLE IF EXISTS Passes CASCADE;
DROP TABLE IF EXISTS Teams CASCADE;
DROP TABLE IF EXISTS Players CASCADE;
DROP TABLE IF EXISTS Dribbles CASCADE;
DROP TABLE IF EXISTS DribbledPast CASCADE;


CREATE TABLE Competitions (
	id INTEGER PRIMARY KEY,
	competition_id INTEGER,
	competition_name VARCHAR(255),
	competition_gender VARCHAR(255),
	
	country_name VARCHAR(255),
	
	season_id INTEGER UNIQUE,	-- Can only have 1 primary key
	season_name VARCHAR(255)
	
	--match_updated DATE, 	-- Unable to use DATETIME
	--match_available DATE	-- Unable to use DATETIME
);


CREATE TABLE Matches (
	match_id INTEGER PRIMARY KEY,
	id INTEGER,
	
	competition_id INTEGER,
	competition_name VARCHAR(255),
	
	country_name VARCHAR(255),
	
	season_id INTEGER,
	season_name VARCHAR(255),
	
	match_date VARCHAR(255),
	kick_off VARCHAR(255),
	
	stadium_id INTEGER,
	stadium_name VARCHAR(255),
	stadium_country VARCHAR(255),
	
	referee_id INTEGER,
	referee_name VARCHAR(255),
	referee_country_id INTEGER,
	referee_country_name VARCHAR(255),
	
	home_team_id INTEGER,
	home_team_name VARCHAR(255),
	home_team_gender VARCHAR(255),
	home_team_manager_id INTEGER,
	home_team_manager_name VARCHAR(255),
	home_team_manager_nickname VARCHAR(255),
	home_team_manager_dob VARCHAR(255),
	home_team_manager_country_id INTEGER,
	home_team_manager_country_name VARCHAR(255),
	home_team_group VARCHAR(255),
	home_team_country_id INTEGER,
	home_team_country_name VARCHAR(255),
	
	away_team_id INTEGER,
	away_team_name VARCHAR(255),
	away_team_gender VARCHAR(255),
	away_team_manager_id INTEGER,
	away_team_manager_name VARCHAR(255),
	away_team_manager_nickname VARCHAR(255),
	away_team_manager_dob VARCHAR(255),
	away_team_manager_country_id INTEGER,
	away_team_manager_country_name VARCHAR(255),
	away_team_group VARCHAR(255),
	away_team_country_id INTEGER,
	away_team_country_name VARCHAR(255),
	
	home_score INTEGER,
	away_score INTEGER,
	match_status VARCHAR(255),
	match_week INTEGER,
	competition_stage_id INTEGER,
	competition_stage_name VARCHAR(255),
	--last_updated DATE, 	-- Unable to use DATETIME
	
	FOREIGN KEY (id) REFERENCES Competitions(id),
	FOREIGN KEY (season_id) REFERENCES Competitions(season_id)
);

CREATE TABLE Teams (
	match_id INTEGER,
    team_id INTEGER PRIMARY KEY,
    team_name VARCHAR(255) UNIQUE,

	FOREIGN KEY (match_id) REFERENCES Matches(match_id)
);

CREATE TABLE Players (
	match_id INTEGER,
    team_id INTEGER,
	team_name VARCHAR(255),
    player_id INTEGER PRIMARY KEY,
    player_name VARCHAR(255) UNIQUE,

	FOREIGN KEY (team_id) REFERENCES Teams(team_id),
	FOREIGN KEY (match_id) REFERENCES Matches(match_id)
);

CREATE TABLE Shots (
	match_id INTEGER,
    statsbomb_xg FLOAT,
    player_id INTEGER,
    player_name VARCHAR(255),
    team_id INTEGER,
    team_name VARCHAR(255),
    first_time BOOLEAN,

	FOREIGN KEY (player_id) REFERENCES Players(player_id),
	FOREIGN KEY (player_name) REFERENCES Players(player_name),
	FOREIGN KEY (team_id) REFERENCES Teams(team_id),
	FOREIGN KEY (team_name) REFERENCES Teams(team_name),
	FOREIGN KEY (match_id) REFERENCES Matches(match_id)
);

CREATE TABLE Passes (
	match_id INTEGER,
    player_id INTEGER,
    player_name VARCHAR(255),
    team_id INTEGER,
    team_name VARCHAR(255),
    through_ball BOOLEAN,
	recipient_id INTEGER,
    recipient_name VARCHAR(255),

	FOREIGN KEY (player_id) REFERENCES Players(player_id),
	FOREIGN KEY (player_name) REFERENCES Players(player_name),
	FOREIGN KEY (team_id) REFERENCES Teams(team_id),
	FOREIGN KEY (team_name) REFERENCES Teams(team_name),
	FOREIGN KEY (match_id) REFERENCES Matches(match_id)
);

CREATE TABLE Dribbles (
	match_id INTEGER,
    player_id INTEGER,
    player_name VARCHAR(255),
    team_id INTEGER,
    team_name VARCHAR(255),
	complete BOOLEAN,

	FOREIGN KEY (player_id) REFERENCES Players(player_id),
	FOREIGN KEY (player_name) REFERENCES Players(player_name),
	FOREIGN KEY (team_id) REFERENCES Teams(team_id),
	FOREIGN KEY (team_name) REFERENCES Teams(team_name),
	FOREIGN KEY (match_id) REFERENCES Matches(match_id)
);

CREATE TABLE DribbledPast (
	match_id INTEGER,
    player_id INTEGER,
    player_name VARCHAR(255),
    team_id INTEGER,
    team_name VARCHAR(255),

	FOREIGN KEY (player_id) REFERENCES Players(player_id),
	FOREIGN KEY (player_name) REFERENCES Players(player_name),
	FOREIGN KEY (team_id) REFERENCES Teams(team_id),
	FOREIGN KEY (team_name) REFERENCES Teams(team_name),
	FOREIGN KEY (match_id) REFERENCES Matches(match_id)
);
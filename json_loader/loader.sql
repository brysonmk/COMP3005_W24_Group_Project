DROP TABLE IF EXISTS Matches;
DROP TABLE IF EXISTS Competitions;


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
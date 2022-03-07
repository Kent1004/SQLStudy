SET FOREIGN_KEY_CHECKS = 0;
ALTER TABLE soccer.coaches
ADD CONSTRAINT coache_fk_1 
FOREIGN KEY (team_id) REFERENCES team(id);

ALTER TABLE soccer.fixture 
ADD CONSTRAINT fixture_fk_1 
FOREIGN KEY (venue_id) REFERENCES soccer.venue(id);

ALTER TABLE soccer.fixture 
ADD CONSTRAINT fixture_fk_2
FOREIGN KEY (referee_id ) REFERENCES soccer.referee(id);

ALTER TABLE soccer.fixture 
ADD CONSTRAINT fixture_fk_3
FOREIGN KEY (home_id ) REFERENCES soccer.team(id);

ALTER TABLE soccer.fixture 
ADD CONSTRAINT fixture_fk_4
FOREIGN KEY (away_id) REFERENCES soccer.team(id);

-- Удаляем игроков , которые на данный момент не имеют команды
delete FROM soccer.player  WHERE team_id NOT IN (SELECT id FROM soccer.team);


ALTER TABLE soccer.player 
ADD CONSTRAINT player_fk_2
FOREIGN KEY (team_id) REFERENCES soccer.team(id);


ALTER TABLE soccer.standings
ADD CONSTRAINT standings_fk_1
FOREIGN KEY (team_id ) REFERENCES soccer.team(id);

ALTER TABLE soccer.statistics
ADD CONSTRAINT statistics_fk_1
FOREIGN KEY (player_id) REFERENCES soccer.player(id);



ALTER TABLE soccer.top_scores
ADD CONSTRAINT top_scores_fk_1
FOREIGN KEY (player _id ) REFERENCES soccer.player(id);

ALTER TABLE soccer.venue 
ADD CONSTRAINT venue_fk_4
FOREIGN KEY (surface_id) REFERENCES soccer.surface(id);


ALTER TABLE soccer.top_scores 
ADD CONSTRAINT top_scores_fk_1
FOREIGN KEY (player_id) REFERENCES soccer.player(id);
SET FOREIGN_KEY_CHECKS = 1;





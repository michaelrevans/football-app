"""
The below is a way to document football leagues, results and tables. The premier league is my example,
but it would be applicable to any league with any number of teams.
"""

class FootballTeam:
    def __init__(self, name):
        self.name = name
        self.points_home = 0
        self.points_away = 0
        self.points_total = 0
        self.goals_for_home = 0
        self.goals_for_away = 0
        self.goals_for_total = 0
        self.goals_against_home = 0
        self.goals_against_away = 0
        self.goals_against_total = 0
        self.goal_diff = 0
        self.games_home = 0
        self.games_away = 0
        self.games_total = 0
        self.wins_home = 0
        self.wins_away = 0
        self.wins_total = 0
        self.losses_home = 0
        self.losses_away = 0
        self.losses_total = 0
        self.draws_home = 0
        self.draws_away = 0
        self.draws_total = 0
        self.all_stats = []

    def __str__(self):
        team_name = str(self.name)
        return team_name

    def get_points(self):
        self.points_total = self.points_home + self.points_away
        return self.points_total

    def get_goals_for(self):
        self.goals_for_total = self.goals_for_home + self.goals_for_away
        return self.goals_for_total

    def get_goals_against(self):
        self.goals_against_total = self.goals_against_home + self.goals_against_away
        return self.goals_against_total

    def get_goal_diff(self):
        self.goal_diff = self.goals_for_total - self.goals_against_total
        return self.goal_diff

    def get_games(self):
        self.games_total = self.games_home + self.games_away
        return self.games_total

    def get_wins(self):
        self.wins_total = self.wins_home + self.wins_away
        return self.wins_total

    def get_draws(self):
        self.draws_total = self.draws_home + self.draws_away
        return self.draws_total

    def get_losses(self):
        self.losses_total = self.losses_home + self.losses_away
        return self.losses_total

    def get_all_stats(self):
        self.goal_diff = self.goals_for_total - self.goals_against_total
        self.all_stats.append(self.name)
        self.all_stats.append(self.get_games())
        self.all_stats.append(self.get_wins())
        self.all_stats.append(self.get_draws())
        self.all_stats.append(self.get_losses())
        self.all_stats.append(self.get_goals_for())
        self.all_stats.append(self.get_goals_against())
        self.all_stats.append(self.get_goal_diff())
        self.all_stats.append(self.get_points())
        return self.all_stats


class FootballLeague:
    def __init__(self, name):
        self.name = name
        self.teams = []
        self.games_played = 0
        self.table = []
        self.results = []

    def __str__(self):
        league_name = "League is " + str(self.name) + "\nTeams are:"
        for team in self.teams:
            league_name += "\n" + str(team)
        return league_name

    def add_team(self, team_name):
        self.teams.append(team_name)

    def add_result(self, team_home, team_away, score_home, score_away):
        if team_home in self.teams and team_away in self.teams:
            if type(score_home) == int and type(score_away) == int:
                self.games_played += 1
                self.results.append([team_home, team_away, score_home, score_away])
                team_home.games_home += 1
                team_home.goals_for_home += score_home
                team_home.goals_against_home += score_away
                team_away.games_away += 1
                team_away.goals_for_away += score_away
                team_away.goals_against_away += score_home
                if score_home > score_away:
                    team_home.points_home += 3
                    team_home.wins_home += 1
                    team_away.losses_away += 1
                elif score_away > score_home:
                    team_away.points_away += 3
                    team_home.losses_home += 1
                    team_away.wins_away += 1
                else:
                    team_home.draws_home += 1
                    team_away.draws_away += 1
                    team_home.points_home += 1
                    team_away.points_away += 1
            else:
                print "Enter valid scores."
        else:
            print "Enter valid teams in " + str(self)

    def get_table(self):
        sorted_table = "Team\t\t\tPlayed\tWon\tDrawn\tLost\tGF\tGA\tGD\tPoints\n"
        for team in self.teams:
            all_info = team.get_all_stats()
            self.table.append(all_info) #self.table a list, all_info a list
        self.table.sort(key = lambda x: (x[8], x[7], x[5])) #sorts self.table by points, GD and then goals scored
        self.table.reverse()
        for row in self.table:
            team_name_string = row.pop(0)
            row_joined = team_name_string + " " * (19 - len(team_name_string)) + "\t" + "\t".join(str(x) for x in row) + "\n" #turns each row (or team) into a string with the relevant info
            sorted_table += row_joined
        return sorted_table

    def get_record(self, team, loc):
        if team in self.teams:
            if loc in ["home", "Home", "H", "h"]:
                team_home_stats = "Home stats:\t" + str(team.name) + "\nPlayed:\t\t" + str(team.games_home) + "\nWon\t\t" + str(team.wins_home) + "\nDrawn:\t\t" + str(team.draws_home) + "\nLost:\t\t" + str(team.losses_home) + "\nGoals for:\t" + str(team.goals_for_home) + "\nGoals against:\t" + str(team.goals_against_home) + "\nGoal diff\t" + str(team.goal_diff) + "\nPoints:\t\t" + str(team.points_home)
                return team_home_stats
            elif loc in ["away", "Away", "A", "a"]:
                team_away_stats = "Away stats:\t" + str(team.name) + "\nPlayed:\t\t" + str(team.games_away) + "\nWon\t\t" + str(team.wins_away) + "\nDrawn:\t\t" + str(team.draws_away) + "\nLost:\t\t" + str(team.losses_away) + "\nGoals for:\t" + str(team.goals_for_away) + "\nGoals against:\t" + str(team.goals_against_away) + "\nGoal diff\t" + str(team.goal_diff) + "\nPoints:\t\t" + str(team.points_away)
                return team_away_stats
            elif loc in ["both", "Both", "all", "All"]:
                team_all_stats = "Total stats:\t" + str(team.name) + "\nPlayed:\t\t" + str(team.games_total) + "\nWon\t\t" + str(team.wins_total) + "\nDrawn:\t\t" + str(team.draws_total) + "\nLost:\t\t" + str(team.losses_total) + "\nGoals for:\t" + str(team.goals_for_total) + "\nGoals against:\t" + str(team.goals_against_total) + "\nGoal diff\t" + str(team.goal_diff) + "\nPoints:\t\t" + str(team.points_total)
                return team_all_stats
            else:
                return "Select a valid location - home, away or both."
        else:
            return "Select a valid team from this league."

    def get_head_to_head(self, team1, team2):
        head_to_head_results = "Head to head results:\n"
        if team1 and team2 in self.teams:
            for record in self.results:
                if (record[0] == team1 and record[1] == team2) or (record[0] == team2 and record[1] == team1):
                    head_to_head_results += str(record[0]) + " " * (19 - len(str(record[0]))) + "\t" + str(record[2]) + "\n"
                    head_to_head_results += str(record[1]) + " " * (19 - len(str(record[1]))) + "\t" + str(record[3]) + "\n\n"
            return head_to_head_results
        else:
            return "Enter two valid teams to compare their results."


ars = FootballTeam("Arsenal")
avi = FootballTeam("Aston Villa")
bou = FootballTeam("Bournemouth")
che = FootballTeam("Chelsea")
cry = FootballTeam("Crystal Palace")
eve = FootballTeam("Everton")
lei = FootballTeam("Leicester")
liv = FootballTeam("Liverpool")
mnc = FootballTeam("Manchester City")
mnu = FootballTeam("Manchester United")
new = FootballTeam("Newcastle")
nor = FootballTeam("Norwich")
sou = FootballTeam("Southampton")
sto = FootballTeam("Stoke")
sun = FootballTeam("Sunderland")
swa = FootballTeam("Swansea")
tot = FootballTeam("Tottenham")
wat = FootballTeam("Watford")
wba = FootballTeam("West Brom")
whu = FootballTeam("West Ham")

prem = FootballLeague("Premier League")

prem.add_team(ars)
prem.add_team(avi)
prem.add_team(bou)
prem.add_team(che)
prem.add_team(cry)
prem.add_team(eve)
prem.add_team(lei)
prem.add_team(liv)
prem.add_team(mnc)
prem.add_team(mnu)
prem.add_team(new)
prem.add_team(nor)
prem.add_team(sou)
prem.add_team(sto)
prem.add_team(sun)
prem.add_team(swa)
prem.add_team(tot)
prem.add_team(wat)
prem.add_team(wba)
prem.add_team(whu)

print prem

prem.add_result(mnu, tot, 1, 0)
prem.add_result(bou, avi, 0, 1)
prem.add_result(eve, wat, 2, 2)
prem.add_result(lei, sun, 4, 2)
prem.add_result(nor, cry, 1, 3)
prem.add_result(che, swa, 2, 2)
prem.add_result(ars, whu, 0, 2)
prem.add_result(new, sou, 2, 2)
prem.add_result(sto, liv, 0, 1)
prem.add_result(wba, mnc, 0, 3)
prem.add_result(avi, mnu, 0, 1)
prem.add_result(sou, eve, 0, 3)
prem.add_result(sun, nor, 1, 3)
prem.add_result(swa, new, 2, 0)
prem.add_result(tot, sto, 2, 2)
prem.add_result(wat, wba, 0, 0)
prem.add_result(whu, lei, 1, 2)
prem.add_result(cry, ars, 1, 2)
prem.add_result(mnc, che, 3, 0)
prem.add_result(liv, bou, 1, 0)
prem.add_result(mnu, new, 0, 0)
prem.add_result(cry, avi, 2, 1)
prem.add_result(lei, tot, 1, 1)
prem.add_result(nor, sto, 1, 1)
prem.add_result(sun, swa, 1, 1)
prem.add_result(whu, bou, 3, 4)
prem.add_result(wba, che, 2, 3)
prem.add_result(eve, mnc, 0, 2)
prem.add_result(wat, sou, 0, 0)
prem.add_result(ars, liv, 0, 0)
prem.add_result(new, ars, 0, 1)
prem.add_result(avi, sun, 2, 2)
prem.add_result(bou, lei, 1, 1)
prem.add_result(che, cry, 1, 2)
prem.add_result(liv, whu, 0, 3)
prem.add_result(mnc, wat, 2, 0)
prem.add_result(sto, wba, 0, 1)
prem.add_result(tot, eve, 0, 0)
prem.add_result(sou, nor, 3, 0)
prem.add_result(swa, mnu, 2, 1)
prem.add_result(eve, che, 3, 1)
prem.add_result(ars, sto, 2, 0)
prem.add_result(cry, mnc, 0, 1)
prem.add_result(nor, bou, 3, 1)
prem.add_result(wat, swa, 1, 0)
prem.add_result(wba, sou, 0, 0)
prem.add_result(mnu, liv, 3, 1)
prem.add_result(sun, tot, 0, 1)
prem.add_result(lei, avi, 3, 2)
prem.add_result(whu, new, 2, 0)
prem.add_result(che, ars, 2, 0)
prem.add_result(avi, wba, 0, 1)
prem.add_result(bou, sun, 2, 0)
prem.add_result(new, wat, 1, 2)
prem.add_result(sto, lei, 2, 2)
prem.add_result(swa, eve, 0, 0)
prem.add_result(mnc, whu, 1, 2)
prem.add_result(tot, cry, 1, 0)
prem.add_result(liv, nor, 1, 1)
prem.add_result(sou, mnu, 2, 3)
prem.add_result(tot, mnc, 4, 1)
prem.add_result(lei, ars, 2, 5)
prem.add_result(liv, avi, 3, 2)
prem.add_result(mnu, sun, 3, 0)
prem.add_result(sou, swa, 3, 1)
prem.add_result(sto, bou, 2, 1)
prem.add_result(whu, nor, 2, 2)
prem.add_result(new, che, 2, 2)
prem.add_result(wat, cry, 0, 1)
prem.add_result(wba, eve, 2, 3)
prem.add_result(cry, wba, 2, 0)
prem.add_result(avi, sto, 0, 1)
prem.add_result(bou, wat, 1, 1)
prem.add_result(mnc, new, 6, 1)
prem.add_result(nor, lei, 1, 2)
prem.add_result(sun, whu, 2, 2)
prem.add_result(che, sou, 1, 3)
prem.add_result(eve, liv, 1, 1)
prem.add_result(ars, mnu, 3, 0)
prem.add_result(swa, tot, 2, 2)
prem.add_result(tot, liv, 0, 0)
prem.add_result(che, avi, 2, 0)
prem.add_result(cry, whu, 1, 3)
prem.add_result(eve, mnu, 0, 3)
prem.add_result(mnc, bou, 5, 1)
prem.add_result(sou, lei, 2, 2)
prem.add_result(wba, sun, 1, 0)
prem.add_result(wat, ars, 0, 3)
prem.add_result(new, nor, 6, 2)
prem.add_result(swa, sto, 0, 1)
prem.add_result(avi, swa, 1, 2)
prem.add_result(lei, cry, 1, 0)
prem.add_result(nor, wba, 0, 1)
prem.add_result(sto, wat, 0, 2)
prem.add_result(whu, che, 2, 1)
prem.add_result(ars, eve, 2, 1)
prem.add_result(sun, new, 3, 0)
prem.add_result(bou, tot, 1, 5)
prem.add_result(mnu, mnc, 0, 0)
prem.add_result(liv, sou, 1, 1)
prem.add_result(che, liv, 1, 3)
prem.add_result(cry, mnu, 0, 0)
prem.add_result(mnc, nor, 2, 1)
prem.add_result(new, sto, 0, 0)
prem.add_result(swa, ars, 0, 3)
prem.add_result(wat, whu, 2, 0)
prem.add_result(wba, lei, 2, 3)
prem.add_result(eve, sun, 6, 2)
prem.add_result(sou, bou, 2, 0)
prem.add_result(tot, avi, 3, 1)
prem.add_result(bou, new, 0, 1)
prem.add_result(lei, wat, 2, 1)
prem.add_result(mnu, wba, 2, 0)
prem.add_result(nor, swa, 1, 0)
prem.add_result(sun, sou, 0, 1)
prem.add_result(whu, eve, 1, 1)
prem.add_result(sto, che, 1, 0)
prem.add_result(avi, mnc, 0, 0)
prem.add_result(ars, tot, 1, 1)
prem.add_result(liv, cry, 1, 2)
prem.add_result(wat, mnu, 1, 2)
prem.add_result(che, nor, 1, 0)
prem.add_result(eve, avi, 4, 0)
prem.add_result(new, lei, 0, 3)
prem.add_result(sou, sto, 0, 1)
prem.add_result(swa, bou, 2, 2)
prem.add_result(wba, ars, 2, 1)
prem.add_result(mnc, liv, 1, 4)
prem.add_result(tot, whu, 4, 1)
prem.add_result(cry, sun, 0, 1)
prem.add_result(avi, wat, 2, 3)
prem.add_result(bou, eve, 3, 3)
prem.add_result(cry, new, 5, 1)
prem.add_result(mnc, sou, 3, 1)
prem.add_result(sun, sto, 2, 0)
prem.add_result(lei, mnu, 1, 1)
prem.add_result(tot, che, 0, 0)
prem.add_result(whu, wba, 1, 1)
prem.add_result(liv, swa, 1, 0)
prem.add_result(nor, ars, 1, 1)

# print prem.get_table()

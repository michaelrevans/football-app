from __future__ import unicode_literals

from django.db import models

# Create your models here.

class FootballTeam(models.Model):
    name = models.CharField(max_length=64)
    points_home = models.PositiveIntegerField()
    points_away = models.PositiveIntegerField()
    points_total = models.PositiveIntegerField()
    goals_for_home = models.PositiveIntegerField()
    goals_for_away = models.PositiveIntegerField()
    goals_for_total = models.PositiveIntegerField()
    goals_against_home = models.PositiveIntegerField()
    goals_against_away = models.PositiveIntegerField()
    goals_against_total = models.PositiveIntegerField()
    goal_diff = models.IntegerField()
    games_home = models.PositiveIntegerField()
    games_away = models.PositiveIntegerField()
    games_total = models.PositiveIntegerField()
    wins_home = models.PositiveIntegerField()
    wins_away = models.PositiveIntegerField()
    wins_total = models.PositiveIntegerField()
    losses_home = models.PositiveIntegerField()
    losses_away = models.PositiveIntegerField()
    losses_total = models.PositiveIntegerField()
    draws_home = models.PositiveIntegerField()
    draws_away = models.PositiveIntegerField()
    draws_total = models.PositiveIntegerField()

    def __unicode__(self):
        return self.name

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

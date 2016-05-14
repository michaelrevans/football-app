from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class FootballTeam(models.Model):
    name = models.CharField(max_length=64)
    points_home = models.PositiveIntegerField(default=0)
    points_away = models.PositiveIntegerField(default=0)
    points_total = models.PositiveIntegerField(default=0)
    goals_for_home = models.PositiveIntegerField(default=0)
    goals_for_away = models.PositiveIntegerField(default=0)
    goals_for_total = models.PositiveIntegerField(default=0)
    goals_against_home = models.PositiveIntegerField(default=0)
    goals_against_away = models.PositiveIntegerField(default=0)
    goals_against_total = models.PositiveIntegerField(default=0)
    goal_diff = models.IntegerField(default=0)
    games_home = models.PositiveIntegerField(default=0)
    games_away = models.PositiveIntegerField(default=0)
    games_total = models.PositiveIntegerField(default=0)
    wins_home = models.PositiveIntegerField(default=0)
    wins_away = models.PositiveIntegerField(default=0)
    wins_total = models.PositiveIntegerField(default=0)
    losses_home = models.PositiveIntegerField(default=0)
    losses_away = models.PositiveIntegerField(default=0)
    losses_total = models.PositiveIntegerField(default=0)
    draws_home = models.PositiveIntegerField(default=0)
    draws_away = models.PositiveIntegerField(default=0)
    draws_total = models.PositiveIntegerField(default=0)

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

    def get_absolute_url(self):
        # return "/teams/%s/" %(self.id)
        return reverse("teams:detail", kwargs={"id": self.id})

from django.contrib import admin

# Register your models here.

from .models import FootballTeam

class TeamModelAdmin(admin.ModelAdmin):
    list_display = ["name", "games_total", "wins_total", "draws_total", "losses_total", "goal_diff", "points_total"]
    class Meta:
        model = FootballTeam

admin.site.register(FootballTeam, TeamModelAdmin)

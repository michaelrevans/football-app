from django import forms

from .models import FootballTeam

class TeamForm(forms.ModelForm):
    class Meta:
        model = FootballTeam
        fields = ["name", "points_total"]

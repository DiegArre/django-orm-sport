from typing import SupportsAbs
from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"ligas_baseball": League.objects.filter(sport="Baseball"),
		"ligas_mujeres" : League.objects.filter(name__contains = "Women"),
		"ligas_hockey": League.objects.filter(name__contains = "Hockey"),
		"ligas_sin_futbol" : League.objects.exclude(sport = "Football"),
		"ligas_conference" : League.objects.filter(name__contains = "Conference"),
		"ligas_atlantica" : League.objects.filter(name__contains= "Atlantic"),
		"equipos_dallas" : Team.objects.filter(location = "Dallas"),
		"equipos_raptor": Team.objects.filter(team_name__contains ="Raptors"),
		"equipos_ciudad" : Team.objects.filter(location__contains = "City")
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
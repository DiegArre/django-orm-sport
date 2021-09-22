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
		"equipos_ciudad" : Team.objects.filter(location__contains = "City"),
		"equipos_t": Team.objects.filter(team_name__startswith ="T"),
		"equipos_order_u" : Team.objects.all().order_by("location"),
		"equipos_order_t" : Team.objects.all().order_by("-team_name"),
		"player_cooper" : Player.objects.filter(last_name = "Cooper"),
		"player_joshua" : Player.objects.filter(first_name = "Joshua"),
		"player_cooper_e" : Player.objects.filter(last_name = "Cooper").exclude(first_name = "Joshua"),
		#SPORTS ORM 2 

		"liga_atlantic" : League.objects.filter(name__contains = "Atlantic"),
		'jugadores_boston': Player.objects.filter(curr_team__team_name="Boston Penguins"),

	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
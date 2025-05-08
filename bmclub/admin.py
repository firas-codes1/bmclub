from django.contrib import admin
from .models import User, Team, Tournament, PlayerMatch, Player, Roles,TeamMatch

#admin.site.register(Users)
admin.site.register(Roles)
admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(Player)
admin.site.register(TeamMatch)
admin.site.register(PlayerMatch)
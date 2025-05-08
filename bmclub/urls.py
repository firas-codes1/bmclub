from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
path('',views.index),
path('pages/login.html', views.login_page),
path('accounts/login/', views.login_page),
path('pages/registration.html', views.sign_up),
path('logout', views.logout_view),
path('newmatch', views.Start_newmatch),
path('newmatch/<slug:slug>/', views.newmatch),
path('newtournament', views.newtor), 
path('newtordoubles', views.newtordoubles),
path('newtorsingles', views.newtorsingles),
path('matchupdate/<slug:matchid>/', views.updatematch), #just see match 
path('matchupdate/<slug:matchid>/<int:playerid>', views.updatematch),
path('profile/', views.profile_view), 
path('player/<int:playerid>', views.playerview), 
path('team/<int:teamid>', views.teamview), 
path('createteam/', views.newteam), 
path('editteam/<int:team_id>', views.editteam), 
path('allmatches/', views.all_matches), 
path('rankings/', views.player_ranking), 
path('mytours/',views.mytours),
path('tournaments/',views.seetours),
path('viewtournament/<int:tournament_id>',views.tournament_detail,name='tournament_detail'),
path('tourchange/<slug:tournament_id>', views.edit_tournament),
path('editplayers/<slug:tournament_id>', views.edit_tournament_players), 
path('approve_player/<slug:tournament_id>/<int:playerid>', views.approve_player), 
path('remove_player/<slug:tournament_id>/<int:playerid>', views.remove_player), 
path('genmatches/<slug:tournament_id>',views.generate_matches),
path('matchchange/<slug:match_id>', views.edit_match),
path('searchteam/', views.searchteams),
path('searchplayer/', views.searchplayers),
path('newcourt/',views.newcourt)

#tournament management (remove/change teams or players), tournament proceedings are automatically done. 

]

from django.shortcuts import render, redirect,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LoginForm, RegisterForm,PlayerMatchForm, TeamMatchForm,Teamform, CourtForm, playerTournamentf, teamTournamentf
from .models import User, Roles, Team, Player, PlayerMatch, TeamMatch, Tournament, playerPool, teamPool, playerholdPool, Court,Court2Tour
import random
import sqlite3 #for development only
from django.core.paginator import Paginator
from django.db.models import Q
#from django.contrib.auth.models import User
#from yourapp.models import Player, Team, Tournament, TeamMatch, PlayerMatch, Roles
from datetime import datetime

def populate():
    Roles.objects.all().delete()  # Delete all roles
    Player.objects.all().delete()  # Delete all players
    Team.objects.all().delete()  # Delete all teams
    Tournament.objects.all().delete()  # Delete all tournaments
    PlayerMatch.objects.all().delete()  # Delete all matches
    TeamMatch.objects.all().delete() 
    User.objects.all().delete()  # Delete all users (be careful with this, as it will remove users)

    # Users Creation
    user1 = User.objects.create_user(username="user1", password="securepassword123", first_name="Hannah", last_name="Baker", email="user1@example.com")
    user2 = User.objects.create_user(username="user2", password="securepassword123", first_name="Alex", last_name="Standal", email="user2@example.com")
    user3 = User.objects.create_user(username="user3", password="securepassword123", first_name="Clay", last_name="Johnson", email="user3@example.com")
    user4 = User.objects.create_user(username="user4", password="securepassword123", first_name="Tony", last_name="Padilla", email="user4@example.com")
    user5 = User.objects.create_user(username="user5", password="securepassword123", first_name="Bryce", last_name="Walker", email="user5@example.com")
    user6 = User.objects.create_user(username="user6", password="securepassword123", first_name="Zachary", last_name="Dempsy", email="user6@example.com")
    user7 = User.objects.create_user(username="user7", password="securepassword123", first_name="Peter", last_name="Griffin", email="user7@example.com")
    user8 = User.objects.create_user(username="user8", password="securepassword123", first_name="Louis", last_name="Griffin", email="user8@example.com")
    user9 = User.objects.create_user(username="user9", password="securepassword123", first_name="Megatron", last_name="Griffin", email="user9@example.com")
    user10 = User.objects.create_user(username="user10", password="securepassword123", first_name="Edward", last_name="Cullen", email="user10@example.com")
    user11 = User.objects.create_user(username="user11", password="securepassword123", first_name="Izabella", last_name="Swan", email="user11@example.com")
    user12 = User.objects.create_user(username="user12", password="securepassword123", first_name="Lance", last_name="Vance", email="user12@example.com")
    user13 = User.objects.create_user(username="user13", password="securepassword123", first_name="Tommy", last_name="Vercetti", email="user13@example.com")
    user14 = User.objects.create_user(username="user14", password="securepassword123", first_name="Stan", last_name="Smith", email="user14@example.com")
    user15 = User.objects.create_user(username="user15", password="securepassword123", first_name="Roger", last_name="ThePhantom", email="user15@example.com")
    user16 = User.objects.create_user(username="user16", password="securepassword123", first_name="jojo", last_name="Siwhat?", email="user16@example.com")
    user17 = User.objects.create_user(username="user17", password="securepassword123", first_name="Morgan", last_name="Wallen", email="user17@example.com")
    user18 = User.objects.create_user(username="user18", password="securepassword123", first_name="Marshall", last_name="Matters", email="user18@example.com")
    user19 = User.objects.create_user(username="user19", password="securepassword123", first_name="Hafez", last_name="Al-Assad jr", email="user19@example.com")
    user20 = User.objects.create_user(username="user20", password="securepassword123", first_name="Bart", last_name="simpson", email="user20@example.com")
     
    
    # Roles Assignment
    referee1 = User.objects.create_user(username="referee1", password="referee123", first_name="Ref Emily", last_name="Refereinkenson", email="referee1@example.com")
    referee2 = User.objects.create_user(username="referee2", password="referee123", first_name="Ref William", last_name="Kicksphere", email="referee2@example.com")
    referee3 = User.objects.create_user(username="referee3", password="referee123", first_name="Ref Grace", last_name="Walker", email="referee3@example.com")
    Roles.objects.create(user=referee1, role="referee")
    Roles.objects.create(user=referee2, role="referee")
    Roles.objects.create(user=referee3, role="referee")

    # 7 Organizers Creation
    organizer1 = User.objects.create_user(username="organizer1", password="organizer123", first_name="John", last_name="doe", email="organizer1@example.com")
    organizer2 = User.objects.create_user(username="organizer2", password="organizer123", first_name="Aleksi", last_name="doe", email="organizer2@example.com")
    organizer3 = User.objects.create_user(username="organizer3", password="organizer123", first_name="Alice", last_name="Wonderland", email="organizer3@example.com")
    organizer4 = User.objects.create_user(username="organizer4", password="organizer123", first_name="DJ", last_name="Trump", email="organizer4@example.com")
    organizer5 = User.objects.create_user(username="organizer5", password="organizer123", first_name="Liam", last_name="Ivanov", email="organizer5@example.com")
    organizer6 = User.objects.create_user(username="organizer6", password="organizer123", first_name="Diego", last_name="O'connor", email="organizer6@example.com")
    organizer7 = User.objects.create_user(username="organizer7", password="organizer123", first_name="Outofnames", last_name="Smith", email="organizer7@example.com")

    # Assign Roles to Organizers
    Roles.objects.create(user=organizer1, role="organizer")
    Roles.objects.create(user=organizer2, role="organizer")
    Roles.objects.create(user=organizer3, role="organizer")
    Roles.objects.create(user=organizer4, role="organizer")
    Roles.objects.create(user=organizer5, role="organizer")
    Roles.objects.create(user=organizer6, role="organizer")
    Roles.objects.create(user=organizer7, role="organizer")

    # 5 Teams Creation
    team1 = Team.objects.create(name="Team 1", TotalScores=0, TotalWins=0)
    team2 = Team.objects.create(name="Team 2", TotalScores=0, TotalWins=0)
    team3 = Team.objects.create(name="Team 3", TotalScores=0, TotalWins=0)
    team4 = Team.objects.create(name="Team 4", TotalScores=0, TotalWins=0)
    team5 = Team.objects.create(name="Team 5", TotalScores=0, TotalWins=0)
    print("Teams created")

    # 10 Players Creation
    player1 = Player.objects.create(user=user1, team=team1, TotalScores=0, TotalWins=0, category="menS")
    player2 = Player.objects.create(user=user2, team=team1, TotalScores=0, TotalWins=0, category="menS")
    player3 = Player.objects.create(user=user3, team=team2, TotalScores=0, TotalWins=0, category="womS")
    player4 = Player.objects.create(user=user4, team=team2, TotalScores=0, TotalWins=0, category="womS")
    player5 = Player.objects.create(user=user5, team=team3, TotalScores=0, TotalWins=0, category="menD")
    player6 = Player.objects.create(user=user6, team=team3, TotalScores=0, TotalWins=0, category="menD")
    player7 = Player.objects.create(user=user7, team=team4, TotalScores=0, TotalWins=0, category="womD")
    player8 = Player.objects.create(user=user8, team=team4, TotalScores=0, TotalWins=0, category="womD")
    player9 = Player.objects.create(user=user9, team=team5, TotalScores=0, TotalWins=0, category="menS")
    player10 = Player.objects.create(user=user10, team=team5, TotalScores=0, TotalWins=0, category="womS")
    
    # Assign Roles to Players
    Roles.objects.create(user=user1, role="player")
    Roles.objects.create(user=user2, role="player")
    Roles.objects.create(user=user3, role="player")
    Roles.objects.create(user=user4, role="player")
    Roles.objects.create(user=user5, role="player")
    Roles.objects.create(user=user6, role="player")
    Roles.objects.create(user=user7, role="player")
    Roles.objects.create(user=user8, role="player")
    Roles.objects.create(user=user9, role="player")
    Roles.objects.create(user=user10, role="player")
    


    # 5 Tournaments Creation
    tournament1 = Tournament.objects.create(tournament_name="Tournament 1", location="Location 1", date=datetime(2023, 5, 15, 9, 0), creator=organizer1)
    tournament2 = Tournament.objects.create(tournament_name="Tournament 2", location="Location 2", date=datetime(2023, 6, 20, 10, 0), creator=organizer1)
    tournament3 = Tournament.objects.create(tournament_name="Tournament 3", location="Location 3", date=datetime(2023, 7, 25, 11, 0), creator=organizer2)
    tournament4 = Tournament.objects.create(tournament_name="Tournament 4", location="Location 4", date=datetime(2023, 8, 30, 12, 0), creator=organizer3)
    tournament5 = Tournament.objects.create(tournament_name="Tournament 5", location="Location 5", date=datetime(2023, 9, 10, 13, 0), creator=organizer4)

    # 10 Matches Creation (5 PlayerMatches and 5 TeamMatches)
    match1 = PlayerMatch.objects.create(player1=player1, player1Score=16, player2=player2, player2Score=13, ref=referee1, tournament=tournament1, player1wins=1, player2wins=0)
    match2 = PlayerMatch.objects.create(player1=player3, player1Score=19, player2=player4, player2Score=14, ref=referee2, tournament=tournament2, player1wins=0, player2wins=1)
    match3 = PlayerMatch.objects.create(player1=player5, player1Score=9, player2=player6, player2Score=5, ref=referee3, tournament=tournament3, player1wins=0, player2wins=0)
    match4 = PlayerMatch.objects.create(player1=player7, player1Score=4, player2=player8, player2Score=8, ref=referee1, tournament=tournament4, player1wins=0, player2wins=0)
    match5 = PlayerMatch.objects.create(player1=player9, player1Score=2, player2=player10, player2Score=0, ref=referee2, tournament=tournament5, player1wins=0, player2wins=0)

    team_match1 = TeamMatch.objects.create(team1=team1, team1Score=21, team2=team2, team2Score=19, ref=referee3, tournament=tournament1, team1wins=1, team2wins=0)
    team_match2 = TeamMatch.objects.create(team1=team3, team1Score=22, team2=team4, team2Score=20, ref=referee1, tournament=tournament2, team1wins=0, team2wins=1)
    team_match3 = TeamMatch.objects.create(team1=team5, team1Score=18, team2=team1, team2Score=21, ref=referee2, tournament=tournament3, team1wins=0, team2wins=0)
    team_match4 = TeamMatch.objects.create(team1=team2, team1Score=23, team2=team4, team2Score=21, ref=referee3, tournament=tournament4, team1wins=0, team2wins=0)
    team_match5 = TeamMatch.objects.create(team1=team3, team1Score=20, team2=team5, team2Score=22, ref=referee1, tournament=tournament5, team1wins=0, team2wins=0)
    print("database populated")



def authentME(usr,pwd):
    conn = sqlite3.connect("badminton.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM auth_user WHERE email = ? AND password = ?", (usr, pwd))
    result = cursor.fetchone()

    if result:
        return User(email=usr)
    #it might be usenrame
    cursor.execute("SELECT * FROM auth_user WHERE username = ? AND password = ?", (usr, pwd))
    result = cursor.fetchone()
    conn.close()   
    if result:
        return User(username=usr)
    else:
        return False

def index(request):
    #print(request.user)
    #populate()
    if request.user.is_authenticated:
        return render(request, 'index.html',{'msg':'user is authenticated'})
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'GET':
        if request.user.is_authenticated: #if user already logged in, redirect other place
            return redirect('/')

        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    elif request.method == 'POST': #if user submitted info to login page
        form = LoginForm(request.POST)  
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #user = authentME(username,password)
            user=authenticate(request,username=username,password=password) #can we put email?
            if user:
                login(request, user)
                messages.success(request,f'welcome back!') #flashing msg
                return redirect('/')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'login.html',{'form': form, 'msg':'Invalid username or password' })


def logout_view(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('/') 


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']  
            playertype= form.cleaned_data['playertype']  

            if ("@" in email)==False:
                return render(request, 'register.html', {'form': form,'msg':'input a valid email'})

            #Create the new user
            user = User.objects.create_user(username=username,email=email, #dont use create_user if youdont want the pwd to be hashed
                password=password,first_name=first_name,last_name=last_name)

            Roles.objects.create(user=user, role=role)
            
            if role=="player":
                team=Team.objects.get(id=1)
                Player.objects.create(user=user,team=team,category=playertype)


            messages.success(request, 'You have singed up successfully.')
            return redirect('login.html')
        else:
            return render(request, 'register.html', {'form': form,'msg':'invalid credentials'})

def is_organizer(user):
    role=Roles.objects.get(user=user)
    if role.role=="organizer":
        return True
    else:
        return False

@user_passes_test(is_organizer)
def Start_newmatch(request):
    return render(request, 'organize1.html')

@user_passes_test(is_organizer)
def newmatch(request,slug):
    if request.method == 'GET':
        if slug=="singles":
            form=PlayerMatchForm()
        else:
            form=TeamMatchForm()
        return render(request, 'organize2.html',{'form': form,})

    if request.method == "POST":
        if slug=="singles":
            form=PlayerMatchForm(request.POST) 
            if form.is_valid()==False:
                return render(request, 'organize2.html',{'form': form,'msg':'You have entered incorrect data',})
            player1=form.cleaned_data['player1']
            player2=form.cleaned_data['player2']
            tournament=form.cleaned_data['tournament']
            player1=Player.objects.get(id=player1)
            player2=Player.objects.get(id=player2)
            tournament=Tournament.objects.get(id=tournament)
            PlayerMatch.objects.create(player1=player1,player2=player2,tournament=tournament)
        else:
            form=TeamMatchForm(request.POST)
            if form.is_valid()==False:
                return render(request, 'organize2.html',{'form': form,'msg':'You have entered incorrect data',})
            team1=form.cleaned_data['player1']
            team2=form.cleaned_data['player2']
            tournament=form.cleaned_data['tournament']
            team1=Team.objects.get(id=team1)
            team2=Team.objects.get(id=team2)
            tournament=Tournament.objects.get(id=tournament)
            TeamMatch.objects.create(team1=team1,team2=team2,tournament=tournament)
        return render(request, 'organize2.html',{'form': form,'msg':'Match created!',})

@user_passes_test(is_organizer)
def newtor(request):
    return render(request, 'newtor.html')

@user_passes_test(is_organizer)
def newtorsingles(request):
    if request.method == 'GET':
        form=playerTournamentf()
        return render(request, 'organize2.html',{'form': form,})

    if request.method == "POST":
        form=playerTournamentf(request.POST) 
        if form.is_valid()==False:   
            return render(request, 'organize2.html',{'form': form,'msg':'You have entered incorrect data',})
        
        tournament_name = form.cleaned_data['tournament_name']
        location = form.cleaned_data['location']
        date=form.cleaned_data['date']
        court=form.cleaned_data['court']
        category=form.cleaned_data['category'] 
        maxparti=form.cleaned_data['maxparti']

        tcourt=Court.objects.get(court=court)
        free=Court2Tour.objects.filter(court=court, tdate=date).exists()
        if free==True:
            return render(request, 'organize2.html',{'form': form,'msg':'Court is reserved at the date you entered: '+str(date),})
        else:
            pass 

        newT=Tournament.objects.create(tournament_name=tournament_name, location=location, date=date,
            creator=request.user,category=category,maxparti=maxparti)
        Court2Tour.objects.create(court=court,tournament=newT,tdate=date) 

        #for player in players:
        #    playerPool.objects.create(tournament=newT,player=player)

        return render(request, 'organize2.html',{'form': form,'msg':'Tournament created!',})

#DElete this probably
@user_passes_test(is_organizer)
def newtordoubles(request):
    if request.method == 'GET':
        form=teamTournamentf()
        return render(request, 'organize2.html',{'form': form,})

    if request.method == "POST":
        form=teamTournamentf(request.POST) 
        if form.is_valid()==False:   
            return render(request, 'organize2.html',{'form': form,'msg':'You have entered incorrect data',})

        tournament_name = form.cleaned_data['tournament_name']
        location = form.cleaned_data['location']
        date=form.cleaned_data['date']
        court=form.cleaned_data['court']
        category=form.cleaned_data['category'] 

        tcourt=Court.objects.get(court=court)
        free=Court2Tour.objects.filter(court=court, tdate=date).exists()
        if free==True:
            return render(request, 'organize2.html',{'form': form,'msg':'Court is reserved at the date you entered: '+str(date),})
        else:
            pass 
        
        newT=Tournament.objects.create(tournament_name=tournament_name, location=location, 
            date=date,
            creator=request.user,category=category)
        Court2Tour.objects.create(court=court,tournament=newT,tdate=date) 
        
        for i in range(1, 9):
            team = form.cleaned_data.get(f'team{i}')
            if team:
                teamPool.objects.create(tournament=newT, team=team)

        #create tournament, then send good msg
        return render(request, 'organize2.html',{'form': form,'msg':'Tournament created!',})


#Maybe add a page solely for viewing the match by players?
#Add page to create new teams, and assign players to teams 
#When a player moves to a team, his total score does not move to the team. 

#for players
def updatematch(request,matchid,playerid=0):
    #first, ensure the user making the request is the organizer of the match
    match = PlayerMatch.objects.get(id=matchid) 
    organizer=PlayerMatch.objects.get(id=matchid).tournament.creator 
    #ref=PlayerMatch.objects.get(id=matchid).ref
    is_referee = Roles.objects.filter(user=request.user, role='referee').exists()
    if (request.user!=organizer) or (is_referee==False):
        return render(request, "matchupdate.html", {'matchinfo':match,'msg':'You are not the organizer or a referee, you cant update results'})
    else:
        if playerid==1:
            match.player1Score += 1
            wincondition=match.player1Score
            if wincondition==21:
                match.player1wins += 1
            match.save()
        elif playerid==2:
            match.player2Score += 1
            wincondition=match.player2Score
            if wincondition==21:
                match.player2wins +=1
            match.save()
        else:
            pass
        return render(request, "matchupdate.html", {'matchinfo':match,'msg':''})

    #then, after every new score, check to see if the player who scored reached 21, if so make him a winner
    #else, continue normally. 
    #when a match is won, call the email notif function, display some msg 

def updateteammatch(request,matchid, teamid=0,playerid=0):
    #first, ensure the user making the request is the organizer of the match 
    match = TeamMatch.objects.get(id=matchid)
    organizer=TeamMatch.objects.get(id=matchid).tournament.creator 
    ref=TeamMatch.objects.get(id=matchid).ref
    if (request.user!=organizer) or (request.user!=ref):
        return render(request, "teammatchupdate.html", {'matchinfo':match,'msg':'You are not the organizer, you cant update results'})
    else:
        if teamid==1:
            match.team1Score += 1
            wincondition=match.team1Score
            #if round was won by team 1
            if wincondition==21:
                match.team1wins += 1
                if match.team1wins==2:
                    match.team1.player1.TotalWins += 1
                    match.team1.player2.TotalWins += 1
                    match.team1.TotalSWins+=1

            #add the score to the player's statistics
            if playerid==1:
                match.team1.player1.TotalScores += 1
                match.team1.TotalScores+=1
            elif playerid==2:
                match.team1.player2.TotalScores += 1
                match.team1.TotalScores+=1
            else:
                pass

            match.save()

        elif teamid==2:
            match.team2Score += 1
            wincondition=match.team2Score
            #if round was won by team 2
            if wincondition==21:
                match.team2wins += 1
                if match.team2wins==2:
                    match.team2.player1.TotalWins += 1
                    match.team2.player2.TotalWins += 1
                    match.team2.TotalSWins+=1

            #add the score to the player's statistics
            if playerid==1:
                match.team2.player1.TotalScores += 1
                match.team2.TotalScores+=1
            elif playerid==2:
                match.team2.player2.TotalScores += 1
                match.team2.TotalScores+=1
            else:
                pass

            match.save()
        else:
            pass
    return render(request, "teammatchupdate.html", {'matchinfo':match,'msg':''})


@login_required
def profile_view(request):
    role = Roles.objects.get(user=request.user).role
    if role=="player":
        player = Player.objects.get(user=request.user)
        return render(request, 'profile.html', {'user': request.user,'role': role, 'player':player})

    return render(request, 'profile.html', {'user': request.user,'role': role, 'player':None})

def playerview(request,playerid):
    player = Player.objects.get(id=playerid)
    return render(request, 'player.html', {'player':player})

def teamview(request,teamid):
    team = Team.objects.get(id=teamid)
    players = Player.objects.filter(team=team)
    
    matches_played = TeamMatch.objects.filter(
        Q(team1=team) | Q(team2=team)
    )
    matches_won = TeamMatch.objects.filter(
    (Q(team1wins=team.id) | Q(team2wins=team.id))
    )
    #SELECT * FROM TeamMatch WHERE Team==TeamMatch.team1 AND TeamMatch.team1wins==2 #same for being team2

    return render(request, 'team.html', {
        'team': team,
        'players': players,
        'matches_played': matches_played,
        'matches_won': matches_won,
    })

@user_passes_test(is_organizer)
def newteam(request):
    if request.method == "POST":
        form = Teamform(request.POST) #instance could be an issue
        if form.is_valid():
            team = Team.objects.create(
                name=form.cleaned_data['name'],
                TotalScores=form.cleaned_data['TotalScores'],
                TotalWins=form.cleaned_data['TotalWins']
            )
            for i in range(1, 5):
                player = form.cleaned_data.get(f'player{i}')
                if player:
                    player.team = team
                    player.save()

            return render(request, 'newteam.html',{"form":Teamform(),'msg':'Team created!'})
        
        else:
            return render(request, 'newteam.html',{"form":Teamform(),'msg':'There was an error!'})

    else:
        return render(request, 'newteam.html',{"form":Teamform(),'msg':''})

@user_passes_test(is_organizer)
def editteam(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    if request.method == "POST":
        form = Teamform(request.POST)
        if form.is_valid():
            # Update team fields
            team.name = form.cleaned_data['name']
            team.TotalScores = form.cleaned_data['TotalScores']
            team.TotalWins = form.cleaned_data['TotalWins']
            team.save()

            # Remove current players from this team
            noteam=Team.objects.get(name="no team")
            Player.objects.filter(team=team).update(team=noteam)

            # Assign new players to the team
            for i in range(1, 5):
                player = form.cleaned_data.get(f'player{i}')
                if player:
                    player.team = team
                    player.save()

            return render(request, 'newteam.html', {"form": form, "msg": "Team updated!", "team": team})
        else:
            return render(request, 'newteam.html', {"form": form, "msg": "Form is invalid!", "team": team})

    else:
        
        initial_data = {
            'name': team.name,
            'TotalScores': team.TotalScores,
            'TotalWins': team.TotalWins,
        }

        players_on_team = list(Player.objects.filter(team=team)[:4])
        for i, player in enumerate(players_on_team, start=1):
            initial_data[f'player{i}'] = player

        form = Teamform(initial=initial_data)
        return render(request, 'newteam.html', {"form": form, "msg": "", "team": team})        

def all_matches(request): 
    singles_matches = PlayerMatch.objects.prefetch_related(
    'player1__user',
    'player2__user',
    'player1wins__user',
    'player2wins__user',
    'ref',
    'tournament',).all()

    doubles_matches = TeamMatch.objects.prefetch_related(
    'team1',
    'team2',
    'team1wins',
    'team2wins',
    'ref',
    'tournament',).all()

    print(doubles_matches)
    return render(request, "all_matches.html", {
        "singles_matches": singles_matches,
        "doubles_matches": doubles_matches
    })


def player_ranking(request):
    # Order players by TotalWins descending
    players = Player.objects.all().order_by('-TotalWins')

    # Paginate with 20 per page
    paginator = Paginator(players, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'ranking.html', {'page_obj': page_obj})

@login_required
def mytours(request):
    tournaments=Tournament.objects.filter(creator=request.user)
    return render(request, "mytours.html", {'tors':tournaments})

@login_required
def edit_tournament(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    tour_court=Court.objects.filter(court2tour__tournament=tournament, 
        court2tour__tdate=tournament.date).first()

    #Check if the tournament is for singles 
    if (tournament.category=="menS") or (tournament.category=="womS"):
        if request.method == "POST":
            form = playerTournamentf(request.POST) #instance could be an issue
            if form.is_valid():

                #check if the court is free on the selected date 
                court=form.cleaned_data['court']
                tdate=form.cleaned_data['date']
                free=Court2Tour.objects.filter(court=court, tdate=tdate).exists()
                if free==True:
                    form = playerTournamentf(initial={'tournament_name':tournament.tournament_name, 
                    'location':tournament.location,    
                    'date':tournament.date,
                    'court':tour_court,
                    'category':tournament.category,
                    'maxparti':tournament.maxparti,})
                    return render(request, "edit_tournament.html", {"form": form, "tournament": tournament, 'msg':'court is reserved at the date'})

                #If court is not reserved on the date
                Court2Tour.objects.filter(tournament=tournament, court=tour_court, tdate=tournament.date).delete()
                
                tournament.tournament_name = form.cleaned_data['tournament_name']
                tournament.location = form.cleaned_data['location']
                tournament.date = tdate
                tournament.category = form.cleaned_data['category']
                tournament.maxparti=form.cleaned_data['maxparti']
                tournament.save() 

                court=Court.objects.get(court=court)

                Court2Tour.objects.create(tournament=tournament,court=court,tdate=tdate)

                return redirect("../mytours/")
        else:
            form = playerTournamentf(initial={'tournament_name':tournament.tournament_name, 
                'location':tournament.location,    
                'date':tournament.date,
                'court':tour_court,
                'category':tournament.category,
                'maxparti':tournament.maxparti,})

        return render(request, "edit_tournament.html", {"form": form, "tournament": tournament})
    

    else:
        teams_in_pool = list(teamPool.objects.filter(tournament=tournament).values_list('team', flat=True))
        team_fields = {}
        for i in range(1, 9):
            team_fields[f'team{i}'] = Team.objects.filter(id=teams_in_pool[i-1]).first() if i <= len(teams_in_pool) else None

        if request.method == "POST":
            form = teamTournamentf(request.POST)
            if form.is_valid():

                #check if the court is free on the selected date 
                court=form.cleaned_data['court']
                tdate=form.cleaned_data['date']
                free=Court2Tour.objects.filter(court=court, tdate=tdate).exists()
                if free==True:
                    initial_data = {
                    'tournament_name': tournament.tournament_name,
                    'location': tournament.location,
                    'date': tournament.date,
                    'court':tour_court,
                    'category': tournament.category,
                    }
                    initial_data.update(team_fields)
                    form = teamTournamentf(initial=initial_data)
                    return render(request, "edit_tournament.html", {"form": form, "tournament": tournament,'msg':'court is reserved at the date'})
            
                #Form is valid, court is free at the date 
                Court2Tour.objects.filter(tournament=tournament, court=tour_court, tdate=tournament.date).delete()
  
                tournament.tournament_name = form.cleaned_data['tournament_name']
                tournament.location = form.cleaned_data['location']
                tournament.date = form.cleaned_data['date']
                tournament.category = form.cleaned_data['category']
                tournament.save()

                court=Court.objects.get(court=court)
                Court2Tour.objects.create(tournament=tournament,court=court,tdate=tdate)

                # Remove old teams and add new ones
                teamPool.objects.filter(tournament=tournament).delete()
                for i in range(1, 9):
                    team = form.cleaned_data.get(f'team{i}')
                    if team:
                        teamPool.objects.create(tournament=tournament, team=team)

                return redirect("../mytours/")
        else:
            initial_data = {
                'tournament_name': tournament.tournament_name,
                'location': tournament.location,
                'date': tournament.date,
                'court':tour_court,
                'category': tournament.category,
            }
            initial_data.update(team_fields)
            form = teamTournamentf(initial=initial_data)
            return render(request, "edit_tournament.html", {"form": form, "tournament": tournament})

def edit_tournament_players(request,tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    if (tournament.category=="menS") or (tournament.category=="womS"):
        players_approved = Player.objects.filter(playerpool__tournament=tournament)
        # Players in hold pool
        players_onhold = Player.objects.filter(playerholdpool__tournament=tournament)

        return render(request, "edit_playersintour.html", 
            {"players": players_approved, "playershold":players_onhold,
            "tournament": tournament})
    
    else:
        #get from team pool 
        teams = Team.objects.filter(teampool__tournament=tournament)
        #put them in a form, and the form should have additional slots for extra teams 
        return render(request, "edit_playersintour.html", 
            {"teams":teams,
            "tournament": tournament})

def approve_player(request, tournament_id,playerid):
    print(playerid)
    player=get_object_or_404(Player, id=playerid)
    tournament = get_object_or_404(Tournament, id=tournament_id)
    inhold= playerholdPool.objects.filter(player=player, tournament=tournament).exists()
    if inhold==True:
        #if the player is in hold, and he is approved 
        playerPool.objects.create(player=player, tournament=tournament) #add player to players pool
        playerholdPool.objects.filter(player=player, tournament=tournament).delete() #remove player from hold pool
    else:
        pass 
    return redirect('../../editplayers/'+str(tournament.id))

def remove_player(request, tournament_id,playerid):
    player=get_object_or_404(Player, id=playerid)
    tournament = get_object_or_404(Tournament, id=tournament_id)
    inhold= playerholdPool.objects.filter(player=player, tournament=tournament).exists()
    inpool=playerPool.objects.filter(player=player, tournament=tournament).exists()
    if inhold==True:
        playerholdPool.objects.filter(player=player, tournament=tournament).delete() #remove player from hold pool
    else:
        pass
    if inpool==True:
        playerPool.objects.filter(player=player, tournament=tournament).delete()
    else:
        pass 
    return redirect('../../editplayers/'+str(tournament.id))

@login_required
def edit_match(request, match_id):
    try:
        match = PlayerMatch.objects.get(id=match_id)
        form_class = PlayerMatchForm
    except PlayerMatch.DoesNotExist:
        match = get_object_or_404(TeamMatch, id=match_id)
        form_class = TeamMatchForm

    if request.method == "POST":
        form = form_class(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect("match_detail", matchid=match.id)
    else:
        form = form_class(instance=match)

    return render(request, "edit_match.html", {"form": form, "match": match})

def searchteams(request,q=""):
    try:
        q = request.GET.get('q', '')
    except:
        pass 

    if q=="":
        teams=[]
    else:
        teams=Team.objects.filter(name__contains=q)
        print("search for teams with name of "+q)
    return render(request, "searchteam.html", {"items": teams,})

def searchplayers(request,q=""):
    try:
        q = request.GET.get('q', '')
    except:
        pass 

    if q=="":
        player=[]
    else:
        player = Player.objects.filter(
        Q(user__first_name__icontains=q) | Q(user__last_name__icontains=q))

    return render(request, "search.html", {"items": player,})

def seetours(request):
    tournaments=Tournament.objects.all()
    paginator = Paginator(tournaments, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "alltours.html", {'tors':tournaments,'page_obj': page_obj})


def tournament_detail(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)

    show_enroll = False
    already_enrolled = False
    matches = []

    try:
        role = Roles.objects.get(user=request.user)
        if role.role == 'player':
            player = Player.objects.get(user=request.user)

            # Check if already enrolled or in hold pool
            in_pool = playerPool.objects.filter(player=player, tournament=tournament).exists()
            in_hold = playerholdPool.objects.filter(player=player, tournament=tournament).exists()

            if not in_pool and not in_hold:
                if tournament.category in ["menS", "womS"]:
                    show_enroll = True
                else:
                    pass
            else:
                already_enrolled = True

            if request.method == 'POST' and 'enroll' in request.POST:
                playerholdPool.objects.create(player=player, tournament=tournament)
                return redirect('../viewtournament/' + str(tournament.id))

    except Roles.DoesNotExist:
        pass
    except Player.DoesNotExist:
        pass

    # Check for matches
    if tournament.category in ["menS", "womS"]:
        matches = PlayerMatch.objects.filter(tournament=tournament)
    else:
        matches = TeamMatch.objects.filter(tournament=tournament)

    return render(request, 'tournament_detail.html', {
        'tournament': tournament,
        'show_enroll': show_enroll,
        'already_enrolled': already_enrolled,
        'matches': matches,
    })

def generate_matches(tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    players = list(playerPool.objects.filter(tournament=tournament).values_list('player', flat=True))
    random.shuffle(players)
    for i in range(0, len(players)-1, 2):
        PlayerMatch.objects.create(
            player1_id=players[i],
            player2_id=players[i+1],
            tournament=tournament,
            duration=30,
        )
    return redirect('../viewtournament/'+str(tournament.id), tournament_id=tournament.id)

@user_passes_test(is_organizer)
def newcourt(request):
    allcourts=Court.objects.all()
    if request.method == 'POST':
        form = CourtForm(request.POST)
        if form.is_valid():
            Court.objects.create(court=form.cleaned_data['court'])
            messages.success(request, 'Court added')
            render(request, 'add_court.html', {'form': form,'msg':'court added','courts':allcourts})
    else:
        form = CourtForm()
    return render(request, 'add_court.html', {'form': form,'msg':'','courts':allcourts})
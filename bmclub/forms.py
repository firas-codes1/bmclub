from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Teamform(forms.Form):
    name = forms.CharField(max_length=255)
    TotalScores= forms.IntegerField()
    TotalWins= forms.IntegerField()
    query=models.Player.objects.all()
    player1 = forms.ModelChoiceField(queryset=query, required=False, label="Player 1")
    player2 = forms.ModelChoiceField(queryset=query, required=False, label="Player 2")
    player3 = forms.ModelChoiceField(queryset=query, required=False, label="Player 3")
    player4 = forms.ModelChoiceField(queryset=query, required=False, label="Player 4")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65,) #widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    ROLE_CHOICES = [
        #('admin', 'Admin'),
        ('player', 'Player'),
        ('organizer', 'Organizer'),
        ('referee', 'Referee'),
    ]
    PLAYER_CHOICES = [
        ('menS', "Men's Singles"),
        ('menD', "Men's Doubles"),
        ('womS', "Women's Singles"),
        ('womD', "Women's Doubles"),
    ]

    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    playertype=forms.ChoiceField(choices=PLAYER_CHOICES)
    #password = forms.CharField(widget=forms.PasswordInput)

class PlayerMatchForm(forms.Form):
    player1 = forms.CharField(max_length=30,label="Player 1 (id)")
    player2 = forms.CharField(max_length=30,label="Player 2 (id)")
    tournament = forms.CharField(max_length=30, label="Tournament (id)")
    matchDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    duration=forms.IntegerField(label="Duration (minutes)")
    #matchTime = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    #status = forms.ChoiceField(choices=[('Scheduled', 'Scheduled'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])

class TeamMatchForm(forms.Form):
    team1 = forms.CharField(max_length=30,label="Team 1 (id)")
    team2 = forms.CharField(max_length=30,label="Team 2 (id)")
    tournament = forms.CharField(max_length=30, label="Tournament (id)")
    matchDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    #matchTime = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    duration=forms.IntegerField(label="Duration (minutes)")
    #status = forms.ChoiceField(choices=[('Scheduled', 'Scheduled'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])

class teamTournamentf(forms.Form):
    PLAYER_CHOICES = [
        #('menS', "Men's Singles"),
        ('menD', "Men's Doubles"),
        #('womS', "Women's Singles"),
        ('womD', "Women's Doubles"),
        ('mix',"Mixed"),
    ]
    tournament_name = forms.CharField(max_length=255)
    location = forms.CharField(max_length=255)
    date=forms.DateTimeField()
    category=forms.ChoiceField(choices=PLAYER_CHOICES)

    query=models.Court.objects.all()
    court=forms.ModelChoiceField(queryset=query, required=True, label="Court")

    query=models.Team.objects.all()
    team1=forms.ModelChoiceField(queryset=query, required=False, label="Team 1")
    team2=forms.ModelChoiceField(queryset=query, required=False, label="Team 2")
    team3=forms.ModelChoiceField(queryset=query, required=False, label="Team 3")
    team4=forms.ModelChoiceField(queryset=query, required=False, label="Team 4")
    team5=forms.ModelChoiceField(queryset=query, required=False, label="Team 5")
    team6=forms.ModelChoiceField(queryset=query, required=False, label="Team 6")
    team7=forms.ModelChoiceField(queryset=query, required=False, label="Team 7")
    team8=forms.ModelChoiceField(queryset=query, required=False, label="Team 8")

#main form used for player tournaments. Teams must be added manually. 
class playerTournamentf(forms.Form):
    PLAYER_CHOICES = [
        ('menS', "Men's Singles"),
        #('menD', "Men's Doubles"),
        ('womS', "Women's Singles"),
        #('womD', "Women's Doubles"),
        ('mix',"Mixed"),
    ]
    tournament_name = forms.CharField(max_length=255)
    location = forms.CharField(max_length=255)
    date=forms.DateTimeField()
    
    query=models.Court.objects.all()
    court=forms.ModelChoiceField(queryset=query, required=True, label="Court")

    category=forms.ChoiceField(choices=PLAYER_CHOICES)
    maxparti=forms.IntegerField(label="Max participants")
    """player1=forms.CharField(max_length=30) 
    player2=forms.CharField(max_length=30) 
    player3=forms.CharField(max_length=30) 
    player4=forms.CharField(max_length=30) 
    player5=forms.CharField(max_length=30) 

    #the view should add the user who created the tournament

    """
    #the view should add the user who created the tournament

#Update Match resutls 
#Note that updating match results should automatically detect win and add the win to team/player and also add scores automatically to player points
#Accessing rankings page creates the ranking through and SQL query. 
class CourtForm(forms.Form):
    court = forms.CharField(max_length=255)

from django.db import models
from django.contrib.auth.models import User

class Team(models.Model): #add a "no team" team for those who dont belong to a team 
    name = models.CharField(max_length=255, unique=True)
    TotalScores= models.IntegerField(default=0)
    TotalWins= models.IntegerField(default=0)
    #player1 = models.ForeignKey('Player', on_delete=models.CASCADE,related_name='team2player1', default=1)
    #player2 = models.ForeignKey('Player', on_delete=models.CASCADE,related_name='team2player2',default=1)
    def __str__(self):
        return self.name

class Player(models.Model):
    ROLE_CHOICES = [
        ('menS', "Men's Singles"),
        ('menD', "Men's Doubles"),
        ('womS', "Women's Singles"),
        ('womD', "Women's Doubles"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    team = models.ForeignKey('Team', on_delete=models.CASCADE,related_name='player2teamxyz')
    TotalScores= models.IntegerField(default=0)
    TotalWins= models.IntegerField(default=0)
    category= models.CharField(max_length=10, choices=ROLE_CHOICES, default='menS')

    def __str__(self):
        return self.user.get_full_name()
#class Player2team(models.Model):
#        team = models.ForeignKey('Team', on_delete=models.CASCADE)


class Roles(models.Model):
    ROLE_CHOICES = [
        #('admin', 'Admin'),
        ('player', 'Player'),
        ('organizer', 'Organizer'),
        ('referee', 'Referee'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='player')


class Tournament(models.Model):
    tournament_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date=models.DateTimeField(null=True, blank=True)
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category=models.CharField(max_length=255,) 
    maxparti=models.IntegerField(default=6)
    #menS womS menT womT mix

class Court(models.Model):
    court=models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.court

class Court2Tour(models.Model):
    tournament= models.ForeignKey('Tournament', on_delete=models.CASCADE)
    court=models.ForeignKey('Court', on_delete=models.CASCADE)
    tdate=models.DateTimeField(null=True, blank=True) #should be the same as tournament date


#should we add an extra team/player to tournament for elimination to work?
class teamPool(models.Model):
    tournament= models.ForeignKey('Tournament', on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

#Holds players participaiting in tournament
class playerPool(models.Model):
    tournament= models.ForeignKey('Tournament', on_delete=models.CASCADE)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)

#This table keeps the players that want to join a tournament but havent been approved by the organizer
class playerholdPool(models.Model):
    tournament= models.ForeignKey('Tournament', on_delete=models.CASCADE)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)   

class TeamMatch(models.Model):
    team1 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='matches_as_team1')
    team1Score=models.IntegerField(default=0)
    team2 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='matches_as_team2')
    team2Score=models.IntegerField(default=0)
    ref = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE)
    team1wins = models.IntegerField(default=0) #models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='teammatches_won1')
    team2wins = models.IntegerField(default=0) #models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='teammatches_won2')
    duration=models.IntegerField(default=0)
    #used to be "winner"
    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.tournament}"

class PlayerMatch(models.Model):
    player1 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='matches_as_player1')
    player1Score=models.IntegerField(default=0)
    player2 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='matches_as_player2')
    player2Score=models.IntegerField(default=0)
    ref = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE)
    player1wins = models.IntegerField(default=0) #models.ForeignKey('Player', on_delete=models.SET_NULL, null=True, blank=True, related_name='playermatches_won1')
    player2wins = models.IntegerField(default=0) #models.ForeignKey('Player', on_delete=models.SET_NULL, null=True, blank=True, related_name='playermatches_won2')
    duration=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.tournament}"

    #Add fields/courts 
    #A field cannot be taken by 2 matches at the same time
    #If there are 5 players, you might want to 
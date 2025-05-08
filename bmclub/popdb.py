from .models import Player, Team, Tournament, TeamMatch, PlayerMatch, Roles
from datetime import datetime

# Create 20 Users
users = []
for i in range(1, 21):
    user = User.objects.create_user(
        username=f"user{i}",
        password="securepassword123",
        first_name=f"FirstName{i}",
        last_name=f"LastName{i}",
        email=f"user{i}@example.com"
    )
    users.append(user)

# Create 3 Referees
referees = []
for i in range(1, 4):
    referee = User.objects.create_user(
        username=f"referee{i}",
        password="referee123",
        first_name=f"RefereeFirstName{i}",
        last_name=f"RefereeLastName{i}",
        email=f"referee{i}@example.com"
    )
    roles = Roles.objects.create(user=referee, role="referee")
    referees.append(referee)

# Create 10 Players and assign them to teams
players = []
teams = []
for i in range(1, 11):
    player_user = users[i - 1]
    team = Team.objects.create(name=f"Team {i}", TotalScores=0, TotalWins=0)
    players.append(
        Player.objects.create(
            user=player_user,
            team=team,
            TotalScores=0,
            TotalWins=0,
            category="menS" if i % 2 == 0 else "womS"
        )
    )
    teams.append(team)

# Create 7 Organizers
organizers = []
for i in range(1, 8):
    organizer = User.objects.create_user(
        username=f"organizer{i}",
        password="organizer123",
        first_name=f"OrganizerFirstName{i}",
        last_name=f"OrganizerLastName{i}",
        email=f"organizer{i}@example.com"
    )
    roles = Roles.objects.create(user=organizer, role="organizer")
    organizers.append(organizer)

# Create 5 Teams
teams = []
for i in range(1, 6):
    team = Team.objects.create(name=f"Team {i}", TotalScores=0, TotalWins=0)
    teams.append(team)

# Create 5 Tournaments
tournaments = []
for i in range(1, 6):
    tournament = Tournament.objects.create(
        tournament_name=f"Tournament {i}",
        location=f"Location {i}",
        date=datetime(2023, 5, 15, 9, 0),  # Example date
        creator=users[i - 1]
    )
    tournaments.append(tournament)

# Create 10 Matches (5 PlayerMatches and 5 TeamMatches)
matches = []
for i in range(1, 6):
    # Create Player Matches
    player_match = PlayerMatch.objects.create(
        player1=players[i - 1],
        player1Score=21,
        player2=players[i + 5],  # Assuming players 6-10 play against players 1-5
        player2Score=18,
        ref=referees[i % 3],  # Rotate referees
        tournament=tournaments[i % 5],
        player1wins=players[i - 1],
        player2wins=None
    )
    matches.append(player_match)

    # Create Team Matches
    team_match = TeamMatch.objects.create(
        team1=teams[i - 1],
        team1Score=21,
        team2=teams[i % 5],  # Rotating teams
        team2Score=19,
        ref=referees[i % 3],  # Rotate referees
        tournament=tournaments[i % 5],
        team1wins=teams[i - 1],
        team2wins=None
    )
    matches.append(team_match)

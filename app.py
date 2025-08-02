
import pandas as pd
import random

print('Reading CSV...')
df = pd.read_csv('Teams.csv')


class Team:
    def __init__(self,name,town,stadium):
        self.name = name
        self.town = town
        self.stadium = stadium
        self.teams_played = []

teams = []

#Iterates through the CSV file using pandas 'iterrows()' function, then for each row we create an object using the Team class
for index,row in df.iterrows():
    team = Team(row['Team Name'],row['Local Town'],row['Team Stadium'])
    teams.append(team)

print('generating Schedule...')
def generate_schedule(teams):
    schedule = []
    Matches = 0
    n = len(teams)
    total_matches = (n*(n-1)*2)/2
    weekend = 1
    matches_this_weekend = 0
   
    while Matches < total_matches:
        #Checks that there 2 matches have been scheduled already, 
        # if so the weekend counter goes to the next week and matches_this_weekend is reset
        if matches_this_weekend == 2:
            weekend += 1
            matches_this_weekend = 0
            
        team1 = random.choice(teams)
        team2 = random.choice(teams)
        #checks that the teams that have been picked are not the same
        if team1 == team2 :
            continue

        #This ensures that if both teams are from the same town, they should not compete each other unless
        # both have played every other non-local team at least once
        if team1.town == team2.town:
           
            other_towns = [t for t in teams if t.town != team1.town and t != team1 and t != team2]
            team1_played = set([tp["name"] for tp in team1.teams_played if any(t.name == tp["name"] and t.town != team1.town for t in teams)])
            team2_played = set([tp["name"] for tp in team2.teams_played if any(t.name == tp["name"] and t.town != team2.town for t in teams)])
            required = set([t.name for t in other_towns])
            if not (required.issubset(team1_played) and required.issubset(team2_played)):
                continue  

        count = 0
        stadium = team1.stadium
        home_team = team1
        away_team = team2
        # This checks if both teams have played each other before if so we increase the count by one to make the Leg 2 
        
        for team in team1.teams_played:
            if team["name"] == team2.name:
                count += 1
                #This checks where their previous match was to ensure that they switch Home and Away teams
                if team['stadium'] == team1.stadium:
                    stadium = team2.stadium
                    home_team = team2
                    away_team = team1
        # This ensures that teams do not play each other more than twice
        if count < 2:
            
            team1.teams_played.append({"name": team2.name, "stadium": stadium, "leg": count + 1})
            team2.teams_played.append({"name": team1.name, "stadium": stadium, "leg": count + 1})
            match = {
                "Weekend": weekend,
                "Leg": count + 1,
                "Home Team": home_team.name,
                "Away Team": away_team.name,
                "Stadium": stadium,
                "Home Town": home_team.town,
                "Away Town": away_team.town
            }
            schedule.append(match)
            Matches += 1
            matches_this_weekend += 1
    print("Schedulde Successfully generated.")    
    return schedule

schedule = generate_schedule(teams)

df_schedule = pd.DataFrame(schedule)
print("Exporting to CSV...")
df_schedule.to_csv("fixture_schedule.csv", index=False)
print("Successfully exported to CSV.")
print(df_schedule)
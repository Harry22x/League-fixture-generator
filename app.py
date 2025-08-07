import pandas as pd
from schedule_generator import generate_schedule
from export_to_csv import export_schedule_to_csv


class Team:
    def __init__(self, name, town, stadium):
        self.name = name
        self.town = town
        self.stadium = stadium
        self.teams_played = []


def read_teams_from_csv(file_path):
    print('Reading CSV...')
    #Pandas module function read_csv() allows our python program to read the csv file 'Teams.csv'
    df = pd.read_csv(file_path)
    teams = []
    
    #Iterates through the CSV file using pandas 'iterrows()' function, 
    #then for each row we create an object using the Team class
    for _, row in df.iterrows():
        team = Team(row['Team Name'], row['Local Town'], row['Team Stadium'])
        teams.append(team)

    return teams


def main():
    teams = read_teams_from_csv("Teams.csv")
    schedule = generate_schedule(teams)
    export_schedule_to_csv(schedule, "ABCPL_fixture_schedule.csv")


if __name__ == "__main__":
    main()

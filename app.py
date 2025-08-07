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
    df = pd.read_csv(file_path)
    teams = []

    for _, row in df.iterrows():
        team = Team(row['Team Name'], row['Local Town'], row['Team Stadium'])
        teams.append(team)

    return teams


def main():
    teams = read_teams_from_csv("Teams.csv")
    schedule = generate_schedule(teams)
    export_schedule_to_csv(schedule, "fixture_schedule.csv")


if __name__ == "__main__":
    main()

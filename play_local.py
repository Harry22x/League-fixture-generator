

def can_play_local(team1, team2, teams):
    #Checks if two local teams can play against each other
    other_towns = [t for t in teams if t.town != team1.town and t not in [team1, team2]]

    team1_played = set([
        tp["name"] for tp in team1.teams_played
        if any(t.name == tp["name"] and t.town != team1.town for t in teams)
    ])
    team2_played = set([
        tp["name"] for tp in team2.teams_played
        if any(t.name == tp["name"] and t.town != team2.town for t in teams)
    ])

    required = set(t.name for t in other_towns)
    return required.issubset(team1_played) and required.issubset(team2_played)


if __name__ == "__main__":
    can_play_local()
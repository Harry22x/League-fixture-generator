def schedule_match(team1, team2):
    """Handles match setup including leg and home/away logic."""
    count = 0
    stadium = team1.stadium
    home_team = team1
    away_team = team2

     # This checks if both teams have played each other before if so we increase the count by one to make the Leg 2 
    for match in team1.teams_played:
        if match["name"] == team2.name:
            count += 1
            #This checks where their previous match was to ensure that they switch Home and Away teams
            if match["stadium"] == team1.stadium:
                stadium = team2.stadium
                home_team = team2
                away_team = team1

    # This ensures that teams do not play each other more than twice
    if count >= 2:
        return None  

    # Record the match
    team1.teams_played.append({"name": team2.name, "stadium": stadium, "leg": count + 1})
    team2.teams_played.append({"name": team1.name, "stadium": stadium, "leg": count + 1})

    return {
        "Weekend":"",
        "Leg": count + 1,
        "Home Team": home_team.name,
        "Away Team": away_team.name,
        "Stadium": stadium,
        "Home Town": home_team.town,
        "Away Town": away_team.town
    }


if __name__ == "__main__":
    schedule_match()
import random
from match_schedular import schedule_match
from play_local import can_play_local

def generate_schedule(teams):
    print("Generating schedule...")
    schedule = []
    n = len(teams)
    total_matches = (n * (n - 1) * 2) // 2
    weekend = 1
    matches_this_weekend = 0
    matches_played = 0

    while matches_played < total_matches:
        if matches_this_weekend == 2:
            weekend += 1
            matches_this_weekend = 0

        team1 = random.choice(teams)
        team2 = random.choice(teams) 

        if team1 == team2:
            continue

        if team1.town == team2.town and not can_play_local(team1, team2, teams):
            continue

        match = schedule_match(team1, team2)
        if match:
            match["Weekend"] = weekend
            schedule.append(match)
            matches_played += 1
            matches_this_weekend += 1

    print("Schedule successfully generated.")
    return schedule

if __name__ == "__main__":
    generate_schedule()
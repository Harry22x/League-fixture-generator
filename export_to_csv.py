import pandas as pd

def export_schedule_to_csv(schedule, output_file):
    print("Exporting to CSV...")
    df_schedule = pd.DataFrame(schedule)
    df_schedule.to_csv(output_file, index=False)
    print("Successfully exported to CSV.")
    print(df_schedule)

if __name__ == "__main__":
    export_schedule_to_csv()

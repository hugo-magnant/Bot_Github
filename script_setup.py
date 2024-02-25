import subprocess
import random
from datetime import datetime, timedelta

def generate_commit_dates(start_date, end_date):
    delta = end_date - start_date
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        if day.weekday() < 5:  # Du lundi au vendredi
            num_commits = random.randint(0, 0)
        else:  # Samedi et dimanche
            num_commits = random.randint(0, 5)
        for _ in range(num_commits):
            hour = random.randint(8, 22)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            yield day.replace(hour=hour, minute=minute, second=second)

def commit_on_date(commit_date):
    formatted_date = commit_date.strftime("%Y-%m-%dT%H:%M:%S +0100")
    with open('timestamp.txt', 'w') as file:
        file.write(commit_date.strftime("%Y-%m-%d %H:%M:%S"))
    subprocess.run(['git', 'add', 'timestamp.txt'], check=True)
    subprocess.run(['git', 'commit', '--date', formatted_date, '-m', f'Commit du {formatted_date}'], check=True)
    print(f"Commit effectué pour le {commit_date.strftime('%d/%m/%Y à %H:%M:%S')}")

def push_changes():
    subprocess.run(['git', 'push', '--all'], check=True)
    print("Changements poussés vers le dépôt distant.")

if __name__ == "__main__":
    start_date = datetime(2023, 4, 24)
    end_date = datetime(2023, 9, 26)
    last_push_date = start_date
    for commit_date in generate_commit_dates(last_push_date, end_date):
        commit_on_date(commit_date)
        if (commit_date - last_push_date).days >= 30:
            push_changes()
            last_push_date = commit_date
    push_changes()  # Assure un dernier push à la fin du script

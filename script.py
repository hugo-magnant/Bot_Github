import random
import datetime
import os
import time

def schedule_commits():
    today = datetime.datetime.now().date()
    # Détermine si aujourd'hui est un jour de semaine ou le week-end
    if today.weekday() < 5:  # Lundi à vendredi
        num_commits = random.randint(7, 15)
    else:  # Samedi et dimanche
        num_commits = random.randint(3, 10)
    commit_hours = sorted(random.sample(range(8 * 60, 22 * 60), num_commits))
    return [datetime.time(hour // 60, hour % 60) for hour in commit_hours]

def calculate_delay(next_commit):
    now = datetime.datetime.now()
    today = now.date()
    next_commit_time = datetime.datetime.combine(today, next_commit)
    if now > next_commit_time:
        next_commit_time += datetime.timedelta(days=1)
    delay = (next_commit_time - now).total_seconds()
    return max(0, delay)

def perform_commit():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('timestamp.txt', 'w') as f:
        f.write(timestamp)
    os.system('git add timestamp.txt')
    os.system('git commit -m "Update timestamp"')
    os.system('git push origin main')

def main():
    commit_times = schedule_commits()
    print("Commit times:", commit_times)

    for next_commit in commit_times:
        delay = calculate_delay(next_commit)
        print(f"Next commit in {delay} seconds.")
        time.sleep(delay)
        perform_commit()
        print(f"Commit performed at {next_commit}.")

    print("All commits for today have been performed.")

if __name__ == "__main__":
    main()

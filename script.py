import random
import datetime
import os
import time

# Définition de la fonction de log
def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('execution_log.txt', 'a') as log_file:  # 'a' pour append
        log_file.write(f"{timestamp} - {message}\n")

def schedule_commits():
    today = datetime.datetime.now().date()
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

def perform_commit(commit_number):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('timestamp.txt', 'w') as f:
        f.write(timestamp)
    os.system('git add timestamp.txt')
    os.system('git commit -m "Update timestamp"')
    os.system('git push origin main')
    log_message(f"Commit {commit_number} and push performed.")

def main():
    log_message("Script started.")
    commit_times = schedule_commits()
    log_message(f"Number of commits today: {len(commit_times)}. Commit times: {commit_times}")

    for i, next_commit in enumerate(commit_times, start=1):
        delay = calculate_delay(next_commit)
        log_message(f"Sleeping for {delay} seconds before commit {i}.")
        time.sleep(delay)
        perform_commit(i)

    log_message("All commits for today have been performed.")
    log_message("Script ended.")

if __name__ == "__main__":
    main()

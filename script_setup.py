import subprocess
import random
from datetime import datetime, timedelta

def generate_commit_dates(start_date, end_date):
    delta = end_date - start_date
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        num_commits = random.randint(1, 15)
        for _ in range(num_commits):
            hour = random.randint(8, 22)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            yield day.replace(hour=hour, minute=minute, second=second)

def commit_on_date(commit_date):
    formatted_date = commit_date.strftime("%Y-%m-%dT%H:%M:%S +0100")
    # Mettre à jour le fichier timestamp.txt avec un timestamp aléatoire
    with open('timestamp.txt', 'w') as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # Stage le fichier
    subprocess.run(['git', 'add', 'timestamp.txt'], check=True)
    # Créer un commit avec la date spécifiée
    subprocess.run(['git', 'commit', '--date', formatted_date, '-m', f'Commit du {formatted_date}'], check=True)
    # Ajouter un print pour afficher le jour et l'heure du commit
    print(f"Commit effectué pour le {commit_date.strftime('%d/%m/%Y à %H:%M:%S')}")

if __name__ == "__main__":
    start_date = datetime(2023, 2, 26)
    end_date = datetime(2024, 2, 25)
    for commit_date in generate_commit_dates(start_date, end_date):
        commit_on_date(commit_date)
    # Pousser tous les changements, y compris les branches, vers le dépôt distant à la fin du script
    subprocess.run(['git', 'push', '--all'], check=True)
    print("Tous les changements et toutes les branches ont été poussés.")

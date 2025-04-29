# migrations-init.py

import os
import subprocess

def run_migrations():
    print("Применение миграций Django для проекта 'mybooksite'...")

    # Выполнить создание миграций
    subprocess.run(['python', 'manage.py', 'makemigrations'])

    # Применить миграции к базе данных
    subprocess.run(['python', 'manage.py', 'migrate'])

if __name__ == "__main__":
    run_migrations()

import os
import sys
import webbrowser
from django.core.management import execute_from_command_line
from pathlib import Path

# PyInstaller fix
if getattr(sys, 'frozen', False):
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')
    BASE_DIR = Path(sys._MEIPASS)
    STATIC_ROOT = BASE_DIR / 'staticfiles'

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotelfinancemanager.settings')

def main():
    webbrowser.open("http://127.0.0.1:8000")
    execute_from_command_line([
        'manage.py',
        'runserver',
        '127.0.0.1:8000',
        '--noreload'
    ])

if __name__ == "__main__":
    main()


# taskkill /f /im run.exe 2>nul
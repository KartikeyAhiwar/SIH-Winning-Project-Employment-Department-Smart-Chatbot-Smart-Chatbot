from django.core.management.base import BaseCommand
import subprocess

class Command(BaseCommand):
    help = 'Run Streamlit app'

    def handle(self, *args, **options):
        subprocess.run(['streamlit', 'run', 'home\streamlit_app.py'])
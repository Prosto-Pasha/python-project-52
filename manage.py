#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv

from django.core.management.commands.runserver import Command as runserver


# Получаем переменные окружения
load_dotenv()  # PORT
PORT = os.getenv('PORT')


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    runserver.default_port = PORT
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

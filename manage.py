#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys
import os

# Add the parent directory (ROLETA) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roleta.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)



if __name__ == '__main__':
    main()

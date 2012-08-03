#!/usr/bin/env python
import os
import sys

from django.core.management import execute_manager

this_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(this_dir, '..'))

import plutoshare.config.settings as settings

if __name__ == "__main__":
    execute_manager(settings)

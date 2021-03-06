#!/usr/bin/env python
"""Postilion."""

import os
import sys
import subprocess
from setuptools import setup

ACTION = sys.argv[1]


def update_reqs():
    """Updates requirements files."""
    if not os.path.exists('Pipfile'):
        return
    subprocess.check_call('pipenv lock', shell=True)
    subprocess.check_call('pipenv lock -r > tools/pip-requires', shell=True)
    subprocess.check_call(
        'pipenv lock --dev -r > tools/test-requires', shell=True)


if ACTION == "update_requirements":
    update_reqs()
    sys.exit(0)
elif ACTION == "build_sphinx":
    subprocess.check_call('pipenv run pip install -e ".[doc]"', shell=True)
elif 'dist' in ACTION:
    update_reqs()

setup(
    setup_requires=['pbr>=1.9', 'setuptools>=17.1', 'pytest-runner'], pbr=True)

#!/usr/bin/env python
import os
import subprocess

# Check for directories
EXCLUDE = [".git", "static", "tests", "src", "dist", "node_modules", "public", "env"]
DIRS = [x for x in os.listdir() if x not in EXCLUDE and os.path.isdir(x)]
DIRS.append("manage.py")

subprocess.call(["yapf", "-r", "-i"] + DIRS)

#!/usr/bin/env python
import os
import sys
from pylint.lint import Run
# Check for directories
EXCLUDE = [".git", "coverage", "static", "tests", "src", "dist", "node_modules", "public", "env"]
DIRS = [x for x in os.listdir() if x not in EXCLUDE and os.path.isdir(x)]

ARGS = ["--load-plugins", "pylint_django"] + sys.argv[1:]
THRESHOLD = 8 # Set the threshold here manually
run = Run(ARGS + DIRS, do_exit=False)
score = run.linter.stats['global_note'] # Yes this is a terrible name for the score

if score < THRESHOLD:
    print("Score below minimum score %f" % (THRESHOLD))
    sys.exit(1)
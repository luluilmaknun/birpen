#!/usr/bin/env python
import os
import sys
from pylint.lint import Run

# Check for directories
EXCLUDE = [
    ".env",
    ".git",
    ".vscode",
    ".idea",
    "coverage",
    "static",
    "tests",
    "src",
    "dist",
    "node_modules",
    "public",
    "env"
    ]
DIRS = [x for x in os.listdir() if x not in EXCLUDE and os.path.isdir(x)]

DISABLE_CHECKS = [
    "duplicate-code",
    "exec-used",
    "file-ignored",
    "localy-disabled",
    "inconsistent-return-statements",
    "invalid-name",
    "no-member",
    "no-self-use",
    "too-few-public-methods",
    "too-many-ancestors",
    "too-many-arguments",
    "too-many-locals",
    "too-many-function-args",
    "too-many-public-methods",
    "wrong-spelling-in-comment",
    "wrong-spelling-in-docstring"
]
DISABLE_CHECKS_STR = ",".join(DISABLE_CHECKS)
DEFAULT_ARGS = ["--load-plugins=pylint_django", "--disable=" + DISABLE_CHECKS_STR]
ARGS = DEFAULT_ARGS + sys.argv[1:]

THRESHOLD = 10 # Set the threshold here manually
run = Run(ARGS + DIRS, do_exit=False)
score = run.linter.stats['global_note'] # Yes this is a terrible name for the score

if score < THRESHOLD:
    print("Score below minimum score %f" % (THRESHOLD))
    sys.exit(1)
    
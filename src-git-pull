#!/usr/bin/env python
# src-git-pull
# Updates ~/src/ from GitHub repos
#
# Author: Daniel Gonzalez Gasull

import os
import subprocess


def pull_repo(directory):
    os.chdir(subdir)
    # Use git up instead of git pull http://stackoverflow.com/a/15316602/37089
    git_up_1 = 'git remote update -p'
    git_up_2 = 'git merge --ff-only @{u}'
    subprocess.call(git_up_1.split(' '))
    subprocess.call(git_up_2.split(' '))
    os.chdir('..')


os.chdir(os.path.expanduser('~/src/'))
for directory in os.listdir('.'):
    if os.path.isdir(directory) and directory.endswith('gasull.github.com'):
        os.chdir(directory)
        for subdir in os.listdir('.'):
            if os.path.isdir(subdir):
                print('Updating %s/%s:' % (directory, subdir))
                pull_repo(subdir)
        os.chdir('..')

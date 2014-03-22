#!/usr/bin/env python
# src-git-pull
# Updates ~/src/ from GitHub repos
#
# Author: Daniel Gonzalez Gasull

import os
import subprocess


def pull_repo(directory):
    os.chdir(directory)
    print('CWD: %s' % os.getcwd())
    # Use git up instead of git pull http://stackoverflow.com/a/15316602/37089
    git_up_1 = 'git remote update -p'
    git_up_2 = 'git merge --ff-only @{u}'
    subprocess.call(git_up_1.split(' '))
    subprocess.call(git_up_2.split(' '))

    for subdir in os.listdir('.'):
        bundle_path = '%s/bundle' % subdir
        if os.path.isdir(bundle_path):
            # Update bundle if found
            os.chdir(bundle_path)
            print('CWD: %s' % os.getcwd())
            for bundle_dir in os.listdir('.'):
                if os.path.isdir(bundle_dir):
                    os.chdir(bundle_dir)
                    print('CWD: %s' % os.getcwd())
                    print('Updating %s/bundle/%s:' % (subdir, bundle_dir))
                    # git pull b/c there shouldn't be changes in bundle
                    subprocess.call(['git', 'pull'])
                    os.chdir('..')
                    print('CWD: %s' % os.getcwd())
            os.chdir('../..')
            print('CWD: %s' % os.getcwd())

    os.chdir('..')
    print('CWD: %s' % os.getcwd())


os.chdir(os.path.expanduser('~/src/'))
print('CWD: %s' % os.getcwd())
for directory in os.listdir('.'):
    if os.path.isdir(directory) and directory.endswith('gasull.github.com'):
        os.chdir(directory)
        print('CWD: %s' % os.getcwd())
        for subdir in os.listdir('.'):
            if os.path.isdir(subdir):
                print('Updating %s/%s:' % (directory, subdir))
                pull_repo(subdir)
        os.chdir('..')
        print('CWD: %s' % os.getcwd())

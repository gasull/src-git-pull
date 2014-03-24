#!/usr/bin/env python
# src-git-pull
#
# Author: Daniel Gonzalez Gasull
"""
Updates ~/src/ from GitHub repos
"""

__author__ = 'Daniel Gonzalez Gasull'

from distutils import spawn
import os
import subprocess


def git_up_repo(repo_dir):
    """
    Runs git up in directory repo_dir.
    See http://stackoverflow.com/a/15316602/37089 for an explanation of
    git up.
    """
    os.chdir(repo_dir)
    print('CWD: %s' % os.getcwd())
    git_up_1 = 'git remote update -p'
    git_up_2 = 'git merge --ff-only @{u}'
    subprocess.call(git_up_1.split(' '))
    subprocess.call(git_up_2.split(' '))

    for subpath in os.listdir('.'):
        bundle_path = '%s/bundle' % subpath
        if os.path.isdir(bundle_path):
            # Update bundle if found
            os.chdir(bundle_path)
            print('CWD: %s' % os.getcwd())
            for bundle_dir in os.listdir('.'):
                if os.path.isdir(bundle_dir):
                    os.chdir(bundle_dir)
                    print('CWD: %s' % os.getcwd())
                    print('Updating %s/%s:' % (bundle_path, bundle_dir))
                    # git pull b/c there shouldn't be changes in bundle
                    subprocess.call(['git', 'pull'])
                    os.chdir('..')
                    print('CWD: %s' % os.getcwd())
            os.chdir('../..')
            print('CWD: %s' % os.getcwd())

    os.chdir('..')
    print('CWD: %s' % os.getcwd())


def update_local():
    """
    Updates my projects at ~/src/*.gasull.github.com/*
    """
    os.chdir(os.path.expanduser('~/src/'))
    print('CWD: %s' % os.getcwd())
    for subpath in os.listdir('.'):
        if os.path.isdir(subpath) and subpath.endswith('gasull.github.com'):
            os.chdir(subpath)
            print('CWD: %s' % os.getcwd())
            for subdir in os.listdir('.'):
                if os.path.isdir(subdir):
                    print('Updating %s/%s:' % (subpath, subdir))
                    git_up_repo(subdir)
            os.chdir('..')
            print('CWD: %s' % os.getcwd())


def update_remote():
    """
    Updates remote machines
    """
    srcgitpull_path = os.path.expanduser(
        '~/src/src-git-pull.gasull.github.com/src-git-pull'
    )
    is_srcgitpull_present = os.path.isdir(srcgitpull_path)
    is_fab_present = spawn.find_executable('fab')
    if not is_srcgitpull_present:
        print('%s not found' % srcgitpull_path)
    if not is_fab_present:
        print('fab not found')
    if is_fab_present and is_srcgitpull_present:
        os.chdir(srcgitpull_path)
        subprocess.call(['fab', 'update_remotes'])


if __name__ == "__main__":
    update_local()
    update_remote()

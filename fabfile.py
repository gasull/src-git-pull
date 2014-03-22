#!/usr/bin/env python
# update_remotes
# Updates all my remote machines
#
# Author: Daniel Gonzalez Gasull

from fabric.api import env
from fabric.api import run

import settings


env.use_ssh_config = True
env.hosts = settings.ENV_HOSTS
env.warn_only = True


def update_remotes():
    run('~/bin/src-git-pull')

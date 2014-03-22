#!/usr/bin/env python
# update_remotes
# Updates all my remote machines
#
# Author: Daniel Gonzalez Gasull

from fabric import api as fab_api
from fabric import exceptions as fab_ex

import settings


fab_api.env.use_ssh_config = True
fab_api.env.hosts = settings.ENV_HOSTS
fab_api.env.warn_only = True


def update_remotes():
    try:
        fab_api.run('~/bin/src-git-pull')
    except fab_ex.NetworkError as ex:
        print(ex)

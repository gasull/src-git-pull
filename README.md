src-git-pull
============

Run git pull for every project in ~/src/


I keep many of my projects in GitHub repos.  Locally they are in my ~/src/
folder.  The folder structure I keep in ~/src/ is one folder per project, where
the project name is the domain of where the project is deployed, or, if it is
not web project, I make something up that makes sense, similar to the way Java
packages are named, but in reverse.  E.g. src-git-pull.gasull.github.com.

Then inside this folder I clone the remote git repository and also keep other
relevant files that might be left out of the repo for any reason.

The script is written with my ~/src/ folder structure in mind.

You need to install python-git for the script to work.

    sudo aptitude install python-git

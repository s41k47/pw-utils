# pw-utils

This repository is about unix passwords. This script is useful when you try to generate a YAML type list of unix password hashes against usernames.

1. Clone
2. $ cd scripts
3. $ chmod 744 phash.py
4. $ ./phash.py

Alternatively you can put phash.py in your $PATH and run from anywhere...

# NOTE: IF YOU REALLY WANT TO USE IT IN AN ANSIBLE PROJECT THEN JUST EDIT FOLLOWING TWO THINGS BEFORE RUNNING

1. On line 19, replace user_list with your variable name
2. On line 41, replace username and pwhash with your required keyname.

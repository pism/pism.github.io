#!/bin/bash

set -e

if [[ -d ~/.local/lib ]];
then
  echo "~/.local/lib is already present: skipping package installation"
else
  apt-get update

  apt-get install python3-pip

  pip3 install --user -r usermap/requirements.txt
fi

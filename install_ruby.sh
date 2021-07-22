#!/bin/bash

set -e

if [[ -d vendor ]];
then
  echo "Directory 'vendor' is already present: skipping bundle install"
  exit 0
else
  bundle install --path=vendor
fi

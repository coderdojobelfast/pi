#!/bin/sh
set -x
git reset --hard HEAD
git pull
sh rc.sh

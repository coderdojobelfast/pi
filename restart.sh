#!/bin/sh
set -x
git reset --hard HEAD
git pull
cp mc/*.py ~/mcpi/api/python

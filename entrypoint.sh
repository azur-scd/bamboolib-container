#!/bin/bash
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# turn on bash's job control
set -m
  
# Start the primary process and put it in the background
./run-notebook.sh &
  
# Start the helper process
./run-voila.sh
  
# the my_helper_process might need to know how to wait on the
# primary process to start before it does its work and returns
  
  
# now we bring the primary process back into the foreground
# and leave it there
fg %1
#!/bin/bash

echo "Starting trading platform..."

export PYTHONPATH=$PYTHONPATH:~/trading-platform

cd ~/trading-platform/platform/supervisor

python3 platform_supervisor.py

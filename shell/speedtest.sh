#!/usr/bin/env bash
timestamp=$(date +"%Y-%m-%d_%H_%M")
logs_dir=$HOME"/logs/speedtest"
file_name=$logs_dir/$timestamp.log
echo $file_name
speedtest --simple --share > "$file_name"
echo "Results stored in $file_name"
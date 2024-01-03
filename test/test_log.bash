#!/bin/bash
# SPDX-FileCopyrightText: 2023 Siromi463 kimimi.nyan@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 20 ros2 launch mypkg log_talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Successfully wrote '10' to the file'


log_file_path="$dir/ros2_ws/src/mypkg/log.txt"

content=$(cat $log_file_path)
expected_content=$(seq 1 20 | paste -sd '\n' -)

if [ "$content" == "$expected_content" ]; then
    echo "Test passed"
    exit 0
else
    echo "Test failed"
    exit 1
fi

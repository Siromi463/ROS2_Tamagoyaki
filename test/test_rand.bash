#!/bin/bash
# SPDX-FileCopyrightText: 2023 Siromi463 kimimi.nyan@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg rand_talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep -E 'Listen: (0|[1-9][0-9]?|100)'

#!/bin/bash
# SPDX-FileCopyrightText: 2023 Siromi463 kimimi.nyan@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 20 ros2 launch mypkg tohex.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Received value: 10, Hex: 000a'

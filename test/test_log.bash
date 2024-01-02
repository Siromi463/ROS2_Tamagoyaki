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

# ファイルの内容をチェック
if grep -q '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n' log.txt; then
    echo "The file contents are correct."
else
    echo "The file contents are not correct."
    exit 1
fi

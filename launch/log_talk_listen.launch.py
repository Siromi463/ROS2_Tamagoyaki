# SPDX-FileCopyrightText: 2023 Siromi463 kimimi.nyan@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    talker_data = launch_ros.actions.Node(
            package='mypkg',
            executable='talker_data',
            )

    listener_log = launch_ros.actions.Node(
            package='mypkg',
            executable='listener_log',
            output='screen'
            )

    return launch.LaunchDescription([talker_data, listener_log])

# SPDX-FileCopyrightText: 2023 Siromi463 kimimi.nyan@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    talker_rand = launch_ros.actions.Node(
            package='mypkg',
            executable='talker_rand',
            )
    listener_rand = launch_ros.actions.Node(
            package='mypkg',
            executable='listener_rand',
            output='screen'
            )
    listener_even = launch_ros.actions.Node(
            package='mypkg',
            executable='listener_even',
            output='screen'
            )
    listener_prime = launch_ros.actions.Node(
            package='mypkg',
            executable='listener_prime',
            output='screen'
            )

    return launch.LaunchDescription([talker_rand, listener_rand, listener_even, listener_prime])

# SPDX-FileCopyrightText: 2023 Siromi463 kimimi.nyan@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    talker = launch_ros.actions.Node(
            package='mypkg',
            executable='talker',
            )

    converter_tobinary = launch_ros.actions.Node(
            package='mypkg',
            executable='converter_tobinary',
            output='screen'
            )

    return launch.LaunchDescription([talker, converter_tobinary])

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    talker = launch_ros.actions.Node(
            package='mypkg',
            executable='talker_rand',
            )

    listener1 = launch_ros.actions.Node(
            package='mypkg',
            executable='listener_EvenNum',
            output='screen'
            )

    listener2 = launch_ros.actions.Node(
            package='mypkg',
            executable='listener_PrimeNum',
            output='screen'
            )

    listener3 = launch_ros.actions.Node(
            package='mypkg',
            executable='listener_Divisors',
            output='screen'
            )

    return launch.LaunchDescription([talker, listener])

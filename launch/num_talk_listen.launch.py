import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    talker_rand = launch_ros.actions.Node(
            package='mypkg',
            executable='talker_rand',
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
    listener_divisors = launch_ros.actions.Node(
            package='mypkg',
            executable='listener_divisors',
            output='screen'
            )
    answer = launch_ros.actions.Node(
            package='mypkg',
            executable='answer',
            output='screen'
            )

    return launch.LaunchDescription([talker_rand, listener_even, listener_prime, listener_divisors, answer])

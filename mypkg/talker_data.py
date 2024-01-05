# SPDX-FileCopyrightText: 2023 Siromi463 kimimi.nyan@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from std_msgs.msg import Int16

def talker_data():
    rclpy.init()
    node = rclpy.create_node('talker_data')
    publisher = node.create_publisher(Int16, 'chatter', 10)
    timer_period = 0.5  # seconds
    i = 1

    def timer_callback():
        nonlocal i
        msg = Int16()
        msg.data = i
        publisher.publish(msg)
        node.get_logger().info('Publishing: "%d"' % msg.data)
        i += 1

        if i > 20:
            rclpy.shutdown()

    timer = node.create_timer(timer_period, timer_callback)

    rclpy.spin(node)

if __name__ == '__main__':
    talker_data()

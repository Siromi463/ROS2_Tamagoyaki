# SPDX-FileCopyrightText: 2023 Siromi463 kimimi.nyan@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0

def cb():
    global n
    if n <= 20:
        msg = Int16()
        msg.data = n
        pub.publish(msg)
        n += 1
    else:
        rclpy.shutdown()

node.create_timer(0.5, cb)
rclpy.spin(node)

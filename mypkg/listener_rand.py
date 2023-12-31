# SPDX-FileCopyrightText: 2023 Siromi463 kimimi.nyan@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    node.get_logger().info("received: %d" % msg.data)

rclpy.init()
node = Node("listener_rand")
pub = node.create_subscription(Int16, "countup", cb, 10)
try:
    rclpy.spin(node)
except KeyboardInterrupt:
    pass
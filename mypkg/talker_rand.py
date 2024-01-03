# SPDX-FileCopyrightText: 2023 Siromi463 kimimi.nyan@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

rclpy.init()
node = Node("talker_rand")
pub = node.create_publisher(Int16, "chatter", 10)

def cb():
    msg = Int16()
    msg.data = random.randint(0, 100)
    pub.publish(msg)

node.create_timer(3.0, cb)
try:
    rclpy.spin(node)
except KeyboardInterrupt:
    pass

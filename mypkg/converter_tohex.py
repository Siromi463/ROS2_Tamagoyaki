# SPDX-FileCopyrightText: 2023 Siromi463 kimimi.nyan@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from std_msgs.msg import Int16

def listener_callback(msg):
    Hex = format(msg.data, '04x')
    print('Received value: %d, Hex: %s' % (msg.data, Hex), flush=True)

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('converter_tohex')
    subscription = node.create_subscription(
        Int16,
        'chatter',
        listener_callback,
        10)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

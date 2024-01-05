# SPDX-FileCopyrightText: 2023 Siromi463 kimimi.nyan@gmail.com
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from std_msgs.msg import Int16

def listener_callback(msg):
    binary = format(msg.data, '016b')
    print('Received value: %d, Binary: %s' % (msg.data, binary), flush=True)

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('converter_tobinary')
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

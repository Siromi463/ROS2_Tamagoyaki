import rclpy
from std_msgs.msg import Int16

def listener_callback(msg):
    hex = format(msg.data, '04x')
    print('Received value: %d, Hex: %s' % (msg.data, Hex))

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('converter_tohex')
    subscription = node.create_subscription(
        Int16,
        'chatter',
        listener_callback,
        10)
    rclpy.spin(node)

if __name__ == '__main__':
    main()

import rclpy
from std_msgs.msg import Int32

def callback(msg):
    if msg.data % 2 == 0:
        print(f'hint 1:even number')
    else:
        print(f'hint 1:odd number')
    rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('listener_EvenNum')
    subscription = node.create_subscription(Int32, 'number', callback, 10)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()

if __name__ == '__main__':
    main()

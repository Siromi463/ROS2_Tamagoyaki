import rclpy
from std_msgs.msg import Int32
import random

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('talker_rand')
    publisher = node.create_publisher(Int32, 'number', 10)

    msg = Int32()
    msg.data = random.randint(0, 100)  # 0から100までのランダムな整数
    publisher.publish(msg)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

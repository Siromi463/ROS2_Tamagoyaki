import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class NumberTalkerNode(Node):
    def __init__(self):
        super().__init__('number_talker')
        self.publisher = self.create_publisher(Int32, 'number', 10)
        self.timer = self.create_timer(1.0, self.publish_number)

    def publish_number(self):
        msg = Int32()
        msg.data = random.randint(1, 100)  # 1から100までのランダムな整数
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = NumberTalkerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

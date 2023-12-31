import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    if msg.data % 2 == 0:
        node.get_logger().info("\neven")
    else:
        node.get_logger().info("\nodd")

rclpy.init()
node = Node("listener_even")
pub = node.create_subscription(Int16, "countup", cb, 10)
try:
    rclpy.spin(node)
except KeyboardInterrupt:
    pass

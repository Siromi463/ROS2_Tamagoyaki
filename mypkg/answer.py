import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
        node.get_logger().info("answer: %d" % msg.data)

rclpy.init()
node = Node("answer")
pub = node.create_subscription(Int16, "countup", 10)
pub = node.create_subscription(Int16, "cb", 10)
try:
    rclpy.spin(node)
except KeyboardInterrupt:
    pass

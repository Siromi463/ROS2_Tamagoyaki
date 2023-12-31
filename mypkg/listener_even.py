import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    if msg.data % 2 == 0:
        node.get_logger().info("Listen: %d is even" % msg.data)
    else:
        node.get_logger().info("Listen: %d is odd" % msg.data)

rclpy.init()
node = Node("listener_even")
pub = node.create_subscription(Int16, "countup", cb, 10)
try:
    rclpy.spin(node)
except KeyboardInterrupt:
    pass

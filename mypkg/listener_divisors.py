import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def divisors(n):
    i = 1
    divisors = []
    while i <= n:
        if n % i == 0:
            divisors.append(i)
        i += 1
    return divisors

def cb(msg):
    global node
    divs = divisors(msg.data)
    node.get_logger().info("Listen: divisors of %d are %s" % (msg.data, divs))

rclpy.init()
node = Node("listener_divisors")
pub = node.create_subscription(Int16, "countup", cb, 10)
try:
    rclpy.spin(node)
except KeyboardInterrupt:
    pass

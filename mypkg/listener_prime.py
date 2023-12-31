import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def cb(msg):
    global node
    if is_prime(msg.data):
        node.get_logger().info("prime")
    else:
        node.get_logger().info("not prime")

rclpy.init()
node = Node("listener_prime")
pub = node.create_subscription(Int16, "countup", cb, 10)
try:
    rclpy.spin(node)
except KeyboardInterrupt:
    pass

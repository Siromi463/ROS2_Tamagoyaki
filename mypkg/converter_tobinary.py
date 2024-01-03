import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import threading

timer = None

def listener_callback(msg):
    global timer
    binary_value = format(msg.data, '016b')
    print('Received value: %d, Binary: %s' % (msg.data, binary_value))
    if timer is not None:
        timer.cancel()
    timer = threading.Timer(10.0, rclpy.shutdown)
    timer.start()

def main():
    global timer
    rclpy.init()
    node = rclpy.create_node('converter_tobinary')
    subscription = node.create_subscription(
        Int16,
        'chatter',
        listener_callback,
        10)
    timer = threading.Timer(10.0, rclpy.shutdown)
    timer.start()
    rclpy.spin(node)

if __name__ == '__main__':
    main()

import rclpy
from std_msgs.msg import Int32

def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def callback(msg):
    divisors = get_divisors(msg.data)
    print(f'hint 3:divisors = {divisors}')
    rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('listener_Divisors')
    subscription = node.create_subscription(Int32, 'number', callback, 10)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()

if __name__ == '__main__':
    main()

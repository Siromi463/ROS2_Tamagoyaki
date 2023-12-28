import rclpy
from std_msgs.msg import Int32

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

def callback(msg):
    if is_prime(msg.data):
        print(f'hint 2:prime number')
    else:
        print(f'hint 2:not prime number')
    rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('listener_PrimeNum')
    subscription = node.create_subscription(Int32, 'number', callback, 10)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()

if __name__ == '__main__':
    main()

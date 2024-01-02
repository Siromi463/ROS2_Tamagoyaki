import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import threading

def logger(msg):
    float_value = float(msg.data)
    log_entry = f'Received: {float_value}\n'
    with open('log.txt', 'a') as log_file:
        log_file.write(log_entry)
    #print("Successfully wrote to the file.")
    timer.cancel()  # タイマーリセット
    timer = threading.Timer(10.0, rclpy.shutdown)  # 新しいタイマー
    timer.start()  # タイマー開始

def main():
    rclpy.init()
    node = Node('logger')
    subscription = node.create_subscription(Float64, 'chatter', logger, 10)
    timer = threading.Timer(10.0, rclpy.shutdown)  # 10秒間メッセージを受信しなかった場合ノードを終了
    timer.start()  # タイマー開始
    rclpy.spin(node)

if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import threading

timer = None  # グローバル変数としてtimerを初期化

def log_message(msg):
    global timer  # timerをグローバル変数化
    int_value = int(msg.data)
    log_entry = f'{int_value}\n'
    with open('log.txt', 'w') as log_file:
        log_file.write(log_entry)
    print("Successfully wrote to the file.")
    if timer is not None:
        timer.cancel()  # 受信でタイマーリセット
    timer = threading.Timer(10.0, rclpy.shutdown)  # 新しいタイマーを設定
    timer.start()  # タイマーを開始

def main():
    global timer
    rclpy.init()
    node = Node('logger')
    subscription = node.create_subscription(Int16, 'chatter', log_message, 10)
    timer = threading.Timer(10.0, rclpy.shutdown)  # 10秒間メッセージを受信しなかった場合にノードを終了
    timer.start()  # タイマーを開始
    rclpy.spin(node)

if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
    def __init__(self):
        super().__init__("example_listener")
        self.create_subscription(String, "/example_count", self.callback, 10)

    def callback(self, message: String):
        self.get_logger().info(f"Received from `/example_count`: {message.data}")


def main():
    rclpy.init()
    listener = Listener()
    rclpy.spin(listener)
    rclpy.shutdown()

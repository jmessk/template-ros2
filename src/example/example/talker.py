import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__("example_talker")
        self.count = 0
        self.publisher = self.create_publisher(String, "/example_count", 10)
        self.create_timer(1, self.callback)

    def callback(self):
        self.count += 1
        self.publisher.publish(String(data=f"{self.count}"))
        self.get_logger().info(f"Published to `/example_count`: {self.count}")


def main():
    rclpy.init()
    talker = Talker()
    rclpy.spin(talker)
    rclpy.shutdown()

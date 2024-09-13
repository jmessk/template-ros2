import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PubNode(Node):
    def __init__(self):
        super().__init__("example_pub")

        self.__counter = 0
        self.__pub = self.create_publisher(String, "/example", 10)

        self.create_timer(1, self.__callback)

    def __callback(self):
        self.__pub.publish(String(data=f"counter=={self.__counter}"))
        self.__counter += 1

        self.get_logger().info(f"Published to `/example`: {self.__counter}")


def main():
    rclpy.init()
    node = PubNode()
    rclpy.spin(node)
    rclpy.shutdown()

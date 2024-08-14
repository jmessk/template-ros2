from rclpy.node import Node
from std_msgs.msg import String


class PublisherNode(Node):

    def __init__(self):
        super().__init__("camera_node")

        self.__camera_publisher = self.create_publisher(String, "/sample", 10)
        self.__timer = self.create_timer(1, self.__timer_callback)

    def __timer_callback(self):
        self.__camera_publisher.publish(String(data="Hello, world!"))

        self.get_logger().info("Publish: /camera")

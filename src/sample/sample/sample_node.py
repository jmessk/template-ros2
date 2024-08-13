from rclpy.node import Node
from std_msgs.msg import String


class SubscriberNode(Node):
    def __init__(self):
        # Initialize the node with the name "display_node"
        super().__init__("sample_node")

        # Create a subscription to the topic "/sample" with the message type String
        self.create_subscription(String, "/sample", self.__sample_callback, 10)

    def __sample_callback(self, message: String):
        self.get_logger().info(f"Received: {message.data}")

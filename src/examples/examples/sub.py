import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SubNode(Node):
    def __init__(self):
        # Initialize the node with the name "display_node"
        super().__init__("sub_node")

        # Create a subscription to the topic "/sample" with the message type String
        self.create_subscription(String, "/example", self.__callback, 10)

    def __callback(self, message: String):
        self._logger.info(f"SubNode: recieved from `/example`: {message.data}")


def main():
    rclpy.init()
    node = SubNode()
    rclpy.spin(node)
    rclpy.shutdown()

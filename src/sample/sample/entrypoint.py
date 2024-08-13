import rclpy
import os

from .sample_node import SubscriberNode


def main():
    try:
        rclpy.init()
        sample_node = SubscriberNode()
        rclpy.spin(sample_node)

    except Exception as e:
        print(e)

    finally:
        sample_node.destroy_node()
        rclpy.shutdown()
        print("Display node shutdown")

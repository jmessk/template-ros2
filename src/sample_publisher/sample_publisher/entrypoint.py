import rclpy
from .sample_publisher import PublisherNode


def main():
    try:
        rclpy.init()
        publisher = PublisherNode()
        rclpy.spin(publisher)

    except Exception as e:
        print(e)

    finally:
        rclpy.shutdown()

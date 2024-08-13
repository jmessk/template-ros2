import rclpy
import os

from .sample_node import SampleNode


def main():
    try:
        rclpy.init()
        sample_node = SampleNode()
        rclpy.spin(sample_node)

    except Exception as e:
        print(e)

    finally:
        cv2.destroyAllWindows()
        sample_node.destroy_node()
        rclpy.shutdown()
        print("Display node shutdown")

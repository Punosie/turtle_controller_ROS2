#!usr/bin/env python3 
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class AvoidWallNode(Node):
    def __init__(self):
        super().__init__("avoid_wall")
        self.get_logger().info("Avoid Wall started...")


def main(args = None):
    rclpy.init(args=args)
    node = AvoidWallNode()
    rclpy.spin(node)
    rclpy.shutdown()
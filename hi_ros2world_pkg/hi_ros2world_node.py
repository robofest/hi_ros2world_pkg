import rclpy
from rclpy.node import Node

class HelloWorldNode(Node):
    def __init__(self):
        # Initialize the node with the name 'hi_ros2world_node'
        super().__init__('hi_ros2world_node')
        # Create a timer that fires every 1.0 seconds
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        # Log the hello message to the console
        self.get_logger().info('Hello World from ROS2 by CJ')

def main(args=None):
    rclpy.init(args=args)      # Initialize ROS2 communications
    node = HelloWorldNode()    # Instantiate our node
    try:
        rclpy.spin(node)       # Keep the node running
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()    # Cleanup
        rclpy.shutdown()       # Shutdown ROS2 communications

if __name__ == '__main__':
    main()
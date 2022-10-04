
import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist
import client_socket2

client_socket2.message.encode
class TurtlesimPublisher(Node):

    def __init__(self):
        super().__init__('turtlesim_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        client_socket2.message.encode = Twist()
        
        x = client_socket2.message.encode.linear.x 
        
        angular = client_socket2.message.encode.angular.z 

        self.publisher.publish(client_socket2.message.encode)



def main(args=None):
    rclpy.init(args=args)

    turtlesim_publisher = TurtlesimPublisher()
    rclpy.spin(turtlesim_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtlesim_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


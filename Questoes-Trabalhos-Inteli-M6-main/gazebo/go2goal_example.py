import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from math import atan2

MAX_DIFF = 0.1

goals = [(1.0, 2.0),
         (4.0, 5.0),
         (2.0, 1.0),
         (3.0, 3.0),
         (5.0, 1.0),
         (5.0, 4.0),
         (7.0, 8.0),
         (0.0, 0.0)]

class TurtleController(Node):
    def __init__(self, goals):
        super().__init__('subscriber_node')
        self.x, self.y, self.theta = 0.0, 0.0, 0.0
        self.point = 0
        self.point_list = goals

        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic='/cmd_vel',
            qos_profile=10)
        
        self.subscription = self.create_subscription(
            msg_type=Odometry,
            topic='/odom',
            callback=self.listener_callback,
            qos_profile=4)

        self.timer = self.create_timer(
            timer_period_sec=0.02,
            callback=self.publisher_callback)

    def listener_callback(self, msg):
            self.x = msg.pose.pose.position.x
            self.y = msg.pose.pose.position.y
            rot = msg.pose.pose.orientation
            _,_,self.theta = euler_from_quaternion([rot.x,rot.y,rot.z,rot.w])
            self.get_logger().info(f"x={self.x:3f}, y={self.y:3f}")

    def publisher_callback(self):
        goal = Point()
        goal.x = self.point_list[self.point][0]
        goal.y = self.point_list[self.point][1]
        
        inc_x = goal.x - self.x
        inc_y = goal.y - self.y
        angle_to_goal = atan2(inc_y,inc_x)
        
        speed = Twist()
        
        if (abs(inc_x) < MAX_DIFF and abs(inc_y) < MAX_DIFF):
            self.point = 0 if (len(self.point_list) == self.point + 1) else (self.point + 1)
            
        if abs(angle_to_goal - self.theta) > MAX_DIFF:
            speed.linear.x = 0.0
            speed.angular.z = 0.3 if (angle_to_goal - self.theta) > 0.0 else -0.3
        else:
            speed.linear.x = 0.5
            speed.angular.z = 0.0
        self.publisher.publish(speed)



def main(args=None):
    rclpy.init(args=args)
    subscriber_node = TurtleController(goals)
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
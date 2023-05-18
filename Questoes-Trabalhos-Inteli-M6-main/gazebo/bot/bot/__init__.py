import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
MAX_DIFF = 0.2
goals = [1.0, 6.0, 3.0,8.0]
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
    def publisher_callback(self):
        goal = Point()
        speed = Twist()
        goal.x = self.point_list[self.point]
        inc_x = goal.x - self.x
        if self.x <=  goal.x and inc_x >= MAX_DIFF:
            speed.linear.x = 0.5
        elif self.x >=  goal.x and inc_x <= MAX_DIFF:
            speed.linear.x = -0.5
        else:
            speed.linear.x = 0.0
            speed.angular.z = 0.0
            self.point = 0 if (len(self.point_list) == self.point + 1) else (self.point + 1)
        print(f'Estou: {self.x} -> {inc_x},  {self.x <=  goal.x}  {inc_x >= 0.2}, {self.point}')
        self.publisher.publish(speed)
def main(args=None):
    rclpy.init(args=args)
    subscriber_node = TurtleController(goals)
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
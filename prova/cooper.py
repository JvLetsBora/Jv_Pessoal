import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist,Point
from turtlesim.msg import Pose
from fila import Fila
from pilha import Pilha
from math import atan2

MAX_DIFF = 0.1

goals = [[0.0, 0.5],

[0.5, 0.0],

[0.0, 0.5],

[0.5, 0.0],

[0.0, 1.0],

[1.0, 0.0] ]


class TurtleController(Node):
    def __init__(self, _goals):
        super().__init__('subscriber_node')
        self.x, self.y, self.theta = 0.0, 0.0, 0.0
        fila = Fila()
        for a in _goals:
            fila.enqueue(a)
        self.point_list = fila
        self.point_pilha = Pilha()
        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic='turtle1/cmd_vel',
            qos_profile=10)
        
        self.subscription = self.create_subscription(
            msg_type=Pose,
            topic='/turtle1/pose',
            callback=self.listener_callback,
            qos_profile=4)

        self.timer = self.create_timer(
            timer_period_sec=0.002,
            callback=self.publisher_callback)

    def listener_callback(self, msg):
            self.x = msg.x
            self.y = msg.y
            self.theta = msg.theta
            print(f"x:{self.x} ; y:{self.y}")

    def publisher_callback(self):
        goal = Point()
        if len(self.point_list.show()) > 0:
            goal.x, goal.y = self.point_list.chamada()
        else:
            goal.x, goal.y = self.point_pilha.chamada()
            if len(self.point_pilha.show()) > 0:
                self.point_pilha.pop()
            else:
                quit()
        inc_x = goal.x - self.x
        inc_y = goal.y - self.y
        angle_to_goal = atan2(inc_y,inc_x)
        
        speed = Twist()
        
        if (abs(inc_x) < MAX_DIFF and abs(inc_y) < MAX_DIFF):
            a = [goal.x, goal.y]
            self.point_pilha._push(a)
            if len(self.point_list.show())>0:
                self.point_list.dequeue()
            
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
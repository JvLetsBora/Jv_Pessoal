# turtlebot3_burger_launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='launch',
            executable='ros2',
            arguments=['launch', 'turtlebot3_gazebo', 'turtlebot3_burger_launch.yaml'],
            output='screen',
        ),
    ])

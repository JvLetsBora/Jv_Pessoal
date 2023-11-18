import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch', 'turtlebot3_world.launch.py')
        ])
    )

    nav2_launch = ExecuteProcess(
        cmd=[
            'ros2', 'launch', 'turtlebot3_navigation2', 'navigation2.launch.py',
            'use_sim_time:=True', 'map:=teste.yaml'
        ],
        output='screen',
        prefix='gnome-terminal --',
    )

    run_robot_node = Node(
        package='my_package',
        executable='my_node',
        name='run_robot',
        output='screen',
        prefix='gnome-terminal --',
    )

    return LaunchDescription([
        gazebo_launch,
        nav2_launch,
        TimerAction(
            period=2.0,
            actions=[run_robot_node]
        )
    ])

# map_launch.py

from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, RegisterEventHandler, ExecuteProcess, LogInfo
from ament_index_python.packages import get_package_share_directory
from launch.event_handlers import OnProcessExit
import os

def generate_launch_description():
    world_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch', 'turtlebot3_world.launch.py')
        ])
    )

    mapper_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('turtlebot3_cartographer'), 'launch', 'cartographer.launch.py')
        ]),
        launch_arguments={'use_sim_time': 'True'}.items(),
    )

    teleop_node = Node(
        package='turtlebot3_teleop',
        executable='teleop_keyboard',
        output='screen',
        prefix='gnome-terminal --',
    )

    teleop_close_event = RegisterEventHandler(
        OnProcessExit(
            target_action=teleop_node,
            on_exit=[
                LogInfo(msg='Mapa salvo'),
                ExecuteProcess(
                    cmd=['ros2', 'run', 'nav2_map_server', 'map_saver_cli', '-f', 'my_map'],
                    output='screen'
                )
            ]
        )
    )


    return LaunchDescription([
        teleop_node,
        world_robot,
        mapper_launch,
        teleop_close_event
    ])


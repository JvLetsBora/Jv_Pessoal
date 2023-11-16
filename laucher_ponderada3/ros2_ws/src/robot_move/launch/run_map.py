
# run_map.py ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=../resource/Maps/teste.yaml
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription,RegisterEventHandler,ExecuteProcess,LogInfo
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.event_handlers import ( OnShutdown,OnProcessExit)
from launch.substitutions import LocalSubstitution

import subprocess





def generate_launch_description():
    nv2_map = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('turtlebot3_gazebo'), 'launch'),
        '/turtlebot3_world.launch.py'])
    )

    return LaunchDescription([
        nv2_map
    ],
    )


comando = "gnome-terminal -e 'python3 ../robot_move/run.py'"
subprocess.run(comando, shell=True)


comando = "gnome-terminal -e 'ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=teste.yaml'"
subprocess.run(comando, shell=True)